import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    if response.status_code != 200:
        return {
            "error": "City not found or weather service unavailable"
        }

    data = response.json()

    rain = data.get("rain", {}).get("1h", 0)

    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": round(data["main"]["temp"], 1),
        "feels_like": round(data["main"]["feels_like"], 1),
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "main": data["weather"][0]["main"],
        "icon": data["weather"][0]["icon"],
        "wind": data["wind"]["speed"],
        "rain": rain
    }