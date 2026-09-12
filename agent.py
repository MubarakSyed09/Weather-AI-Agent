import ollama
import json
from weather import get_weather

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather information for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

messages = [
    {
        "role": "system",
        "content": "You are a helpful weather AI agent. Use the weather tool when the user asks about weather."
    }
]

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model="llama3.2",
        messages=messages,
        tools=tools
    )

    messages.append(response["message"])

    if response["message"].get("tool_calls"):

        for tool_call in response["message"]["tool_calls"]:

            if tool_call["function"]["name"] == "get_weather":

                city = tool_call["function"]["arguments"]["city"]

                print("Agent is checking weather for:", city)

                result = get_weather(city)

                messages.append({
                    "role": "tool",
                    "content": json.dumps(result)
                })

        final_response = ollama.chat(
            model="llama3.2",
            messages=messages
        )

        print("\nAgent:", final_response["message"]["content"])

    else:

        print("\nAgent:", response["message"]["content"])