import os
from flask import Flask, jsonify, render_template, request
from google import genai
from weather import get_weather

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-2.5-flash"


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
  user_input = request.json.get("message", "").strip()

  if not user_input:
    return jsonify({"error": "Please enter a question."}), 400

  weather_result = {}

  def weather_tool(city: str) -> dict:
    result = get_weather(city)
    weather_result.clear()
    weather_result.update(result)
    return result

  try:
    response = client.models.generate_content(
        model=MODEL,
        contents=user_input,
        config={
            "system_instruction": """
You are an intelligent AI Weather Agent.

Your job is to help users understand current weather.

When the user asks about weather, use the weather_tool.

After receiving weather information:
- Explain the weather clearly.
- Give a short useful recommendation.
- Mention umbrella advice when appropriate.
- Mention clothing or outdoor activity advice when useful.
- Never invent weather information.

If the user asks a normal question that does not require weather,
answer normally without using the weather tool.

Keep answers concise and friendly.
""",
            "tools": [weather_tool],
        },
    )

    return jsonify({
        "answer": response.text,
        "weather": weather_result if weather_result else None,
    })

  except Exception as e:
    print("ERROR:", str(e))
    return jsonify({"error": "AI service temporarily unavailable."}), 500


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port, debug=True)