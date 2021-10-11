"""Инструкции для первого запуска приложения."""

from faker import Faker

from core.models import *
from core.use_cases import create_new_post
from main import create_app

if __name__ == "__main__":
    # Настройка схемы БД.
    app = create_app()
    app.app_context().push()
    db.create_all(app=app)

    # Заполнение фейковыми данными.
    fake = Faker()
    for _ in range(100):
        create_new_post(
            alias=fake.domain_word(),
            title=fake.name(),
            text=fake.text(),
        )
