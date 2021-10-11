"""Основной скрипт для запуска блога."""

from pathlib import Path

from dynaconf import FlaskDynaconf
from flask import Flask
from flask_smorest import Api

# Настройка директории для хранения временных файлов и прочего локального барахла.
LOCAL_TMP_PATH = Path() / "tmp"
LOCAL_TMP_PATH.mkdir(mode=0o755, exist_ok=True)


def create_app(app_config: dict = None):
    """Создание экземпляра приложения."""
    app = Flask(__name__)
    FlaskDynaconf(
        app,
        settings_files=("config/settings.toml", "config/local_settings.toml"),  # Порядок загрузки файлов - последние перекрывают предыдущие.
        MERGE_ENABLED_FOR_DYNACONF=True,
        **(app_config if app_config else {})
    )

    from core.models import db
    db.init_app(app)

    from api.blog import blog_blueprint
    api = Api(app)
    api.register_blueprint(blog_blueprint, url_prefix="/api/blog")

    return app


if __name__ == "__main__":
    create_app({}).run()
