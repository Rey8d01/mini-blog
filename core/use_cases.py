"""Функции выполняющие основные задачи системы."""

from flask import current_app

from core.models import Post, db


def slice_posts():
    """Вернет срез постов блога на указанной странице."""
    with current_app.app_context():
        posts = Post.query.filter_by(is_deleted=False).all()
    return posts


def create_new_post(post_alias: str, post_title: str, post_text: str) -> Post:
    """Сохранит новый пост в блоге."""
    with current_app.app_context():
        new_post = Post(alias=post_alias, title=post_title, text=post_text)
        db.session.add(new_post)
        db.session.commit()
    return new_post


def update_post(old_post_alias: str, new_post_alias: str, post_title: str, post_text: str) -> bool:
    """Обновит информацию в указанном посте."""
    with current_app.app_context():
        post_for_update: Post = Post.query.filter_by(alias=old_post_alias, is_deleted=False).first()
        if post_for_update is None:
            return False

        post_for_update.alias = new_post_alias
        post_for_update.title = post_title
        post_for_update.text = post_text
        db.session.commit()
    return True


def mark_post_deleted(post_alias: str) -> bool:
    """Выполнит операцию удаления поста."""
    with current_app.app_context():
        post_for_delete: Post = Post.query.filter_by(alias=post_alias, is_deleted=False).first()
        if post_for_delete is None:
            return False

        post_for_delete.is_deleted = True
        db.session.commit()
    return True
