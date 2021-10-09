"""Основной скрипт для запуска блога."""

import logging

from flask import Flask

logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/hello")
def hello():
    return "Hello, World"


if __name__ == "__main__":
    app.run(debug=True)
