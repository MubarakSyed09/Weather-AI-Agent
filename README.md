# Weather AI Agent

An AI-powered weather assistant that combines real-time weather data with natural-language interaction. Ask about the weather in any city and get a conversational, intelligent response.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?style=flat&logo=google&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

---

## 📌 Overview

Weather AI Agent is a Python application that wraps the OpenWeatherMap API with an AI agent layer. The agent uses **tool-calling** — where the LLM decides when to call the weather function, processes the result, and returns a natural-language response to the user.

A Flask web server provides the frontend interface, and the project supports both local LLMs via Ollama and cloud-based models via Google Gemini.

---

## 🔧 How It Works

```
User Input (city name / weather question)
        ↓
   Flask App (app.py)
        ↓
   AI Agent (agent.py)    ←── Uses tool-calling
        ↓
   weather.py             ←── Calls OpenWeatherMap API
        ↓
   Structured weather data returned to agent
        ↓
   LLM generates natural-language response
        ↓
   Response displayed to user
```

The agent is built using **Ollama's tool-calling interface**, with the weather retrieval function registered as a callable tool. The LLM decides when to invoke the weather function based on the user's query.

---

## ✨ Features

- Natural-language weather queries ("What should I wear in Mumbai today?")
- Real-time weather data — temperature, humidity, wind, weather conditions
- AI-generated contextual responses using LLM tool-calling
- Flask web interface with static frontend
- API key handled securely via environment variables (`.env`)
- Supports local LLMs via Ollama

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python |
| Web Framework | Flask |
| AI Agent | Ollama (tool-calling) |
| AI API | Google Gemini (`google-genai`) |
| Weather Data | OpenWeatherMap API |
| Environment | `python-dotenv` |
| Production Server | Gunicorn |

---

## 📁 Project Structure

```
Weather-AI-Agent/
├── agent.py          # AI agent with tool-calling logic
├── weather.py        # OpenWeatherMap API integration
├── app.py            # Flask web application
├── templates/        # HTML templates
├── static/           # CSS and frontend assets
├── requirements.txt  # Python dependencies
├── .gitignore        # Ignores .env and secrets
└── README.md
```

---

## 🚀 Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/MubarakSyed09/Weather-AI-Agent.git
cd Weather-AI-Agent
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory:
```env
WEATHER_API_KEY=your_openweathermap_api_key_here
```

> Get a free API key at [openweathermap.org](https://openweathermap.org/api)

**5. Run the application**
```bash
python app.py
```

Open `http://localhost:5000` in your browser.

---

## ⚙️ Requirements

```
Flask
requests
python-dotenv
google-genai
gunicorn
ollama
```

---

## 🔒 Security

- API keys are loaded from environment variables using `python-dotenv`
- Never commit your `.env` file — it is listed in `.gitignore`
- A `.env.example` with placeholder values can be used as a reference

---

## 🚧 Future Improvements

- Add support for multi-city comparisons
- Add weather forecasts (multi-day)
- Improve frontend UI with weather icons and animations
- Add conversation history for multi-turn queries

---

## 👤 Author

**Mubarak Sayyad** — [GitHub](https://github.com/MubarakSyed09)

3rd Year B.Tech CSE student, VFSTR.
