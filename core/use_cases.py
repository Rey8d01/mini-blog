"""Функции выполняющие основные задачи системы."""

from typing import Optional

from flask import current_app

from core.models import Post, db


def create_new_post(alias: str, title: str, text: str) -> Post:
    """Сохранит новый пост в блоге."""
    with current_app.app_context():
        new_post = Post(alias=alias, title=title, text=text)
        db.session.add(new_post)
        db.session.commit()
        created_post = Post.query.get(new_post.id)
    return created_post


def update_post(old_alias: str, new_alias: str, new_title: str, new_text: str) -> Optional[Post]:
    """Обновит информацию в указанном посте."""
    with current_app.app_context():
        post_for_update: Post = Post.query.filter_by(alias=old_alias, is_deleted=False).first()
        if post_for_update is None:
            return None

        post_for_update.alias = new_alias
        post_for_update.title = new_title
        post_for_update.text = new_text
        db.session.commit()

        updated_post = Post.query.get(post_for_update.id)
    return updated_post


def mark_post_deleted(alias: str) -> bool:
    """Выполнит операцию удаления поста."""
    with current_app.app_context():
        post_for_delete: Post = Post.query.filter_by(alias=alias, is_deleted=False).first()
        if post_for_delete is None:
            return False

        post_for_delete.is_deleted = True
        db.session.commit()
    return True
