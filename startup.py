"""Инструкции для первого запуска приложения."""

from faker import Faker

from core.exceptions import PostException
from core.models import *
from core.use_cases import create_new_post
from main import create_app, LOCAL_TMP_PATH

if __name__ == "__main__":
    need_fill_db = False
    if not any(LOCAL_TMP_PATH.iterdir()):
        need_fill_db = True

    # Настройка схемы БД.
    app = create_app()
    app.app_context().push()
    db.create_all(app=app)

    # Заполнение фейковыми данными.
    if need_fill_db:
        fake = Faker()
        for _ in range(100):
            try:
                create_new_post(
                    alias=fake.domain_word(),
                    title=fake.name(),
                    text=fake.text(),
                )
            except PostException:
                pass
