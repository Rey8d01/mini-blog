"""Тестирование основных функций блога."""

import pytest
from flask.testing import FlaskClient

from core.models import db
from core.use_cases import create_new_post, update_post, mark_post_deleted
from main import create_app


@pytest.fixture
def client():
    """Инициализация приложения для теста и локального контекста."""
    app = create_app({"ENV": "testing"})
    app.app_context().push()
    db.create_all(app=app)

    with app.test_client() as client:
        yield client

    db.drop_all(app=app)


def test_create_new_post(client: FlaskClient):
    """Тест создания поста в блог."""
    created_post = create_new_post("test-alias", "Test title", "Test text")
    assert created_post.alias == "test-alias"


def test_update_post(client: FlaskClient):
    """Тест изменения поста в блоге."""
    created_post = create_new_post("test-alias", "Test title", "Test text")
    assert created_post.alias == "test-alias"

    updated_post = update_post("test-alias", "new-test-alias", "Test title", "Test text")
    assert updated_post.alias == "new-test-alias"
    assert created_post.id == updated_post.id


def test_mark_post_deleted(client: FlaskClient):
    """Тест удаления поста в блоге."""
    created_post = create_new_post("test-alias", "Test title", "Test text")
    assert created_post.alias == "test-alias"

    post_deleted_result = mark_post_deleted("test-alias")
    assert post_deleted_result is True
