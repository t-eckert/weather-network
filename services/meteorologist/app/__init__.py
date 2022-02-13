from urllib import response
from dotenv import load_dotenv
from flask import Flask
from os import environ

import httpx

load_dotenv()
weather_api_key = environ["OPEN_WEATHER_API_KEY"]

app = Flask(__name__)


def fetch_location() -> str | None:
    response = httpx.get("https://ipinfo.io/json")
    if response.status_code == 200:
        return response.json()["loc"]
    return None


def fetch_weather(location: str) -> dict | None:
    lat, lon = location.split(",")

    response = httpx.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric"
    )

    if response.status_code == 200:
        return response.json()
    return None


@app.route("/")
def index() -> dict | None:
    location = fetch_location()
    weather = fetch_weather(location)
    return weather
