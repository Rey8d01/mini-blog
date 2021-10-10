"""Инструкции для первого запуска приложения."""

from core.models import *
from main import create_app

if __name__ == "__main__":
    # Настройка схемы БД.
    db.create_all(app=create_app())
