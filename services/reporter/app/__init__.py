from cmath import log
from dotenv import load_dotenv
from flask import Flask, jsonify
from os import environ

import httpx

load_dotenv()
host = environ["HOST"]
ports = environ["PORTS"].split(",")

app = Flask(__name__)


def get_nodes():
    return [f"{host}:{port}" for port in ports]


@app.route("/")
def index():
    weather_reports = {}
    for node in get_nodes():
        try:
            response = httpx.get(node)
            if response.status_code == 200:
                name = response.json()["name"]
                weather_reports[name] = response.json()
        except Exception as e:
            app.log_exception(e)
    return jsonify(weather_reports)
