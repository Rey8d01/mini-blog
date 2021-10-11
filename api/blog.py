"""REST API для блога."""

import marshmallow as ma
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_smorest.pagination import PaginationParameters
from marshmallow import validate

from core.exceptions import PostException
from core.models import Post
from core.use_cases import create_new_post, update_post, mark_post_deleted

blog_blueprint = Blueprint("blog", __name__, url_prefix="/blog", description="Blog")


class PostSchema(ma.Schema):
    """Схема поста в блоге для отображения клиенту."""

    id = ma.fields.Int(dump_only=True)
    alias = ma.fields.String()
    title = ma.fields.String()
    text = ma.fields.String()
    created = ma.fields.DateTime()
    updated = ma.fields.DateTime()


class PostQuerySchema(ma.Schema):
    """Схема для параметров запроса поста."""

    alias = ma.fields.String(validate=validate.Length(max=120))


class PostArgsSchema(ma.Schema):
    """Схема для создания нового поста."""

    alias = ma.fields.String(validate=validate.Length(max=120))
    title = ma.fields.String(validate=validate.Length(max=200))
    text = ma.fields.String()


@blog_blueprint.route("/posts")
class Posts(MethodView):
    """Постраничная выдача постов."""

    @blog_blueprint.response(200, PostSchema(many=True))
    @blog_blueprint.paginate(page=1, page_size=10, max_page_size=20)
    def get(self, pagination_parameters: PaginationParameters):
        """Список постов в блоге."""
        interesting_posts = Post \
            .query \
            .filter_by(is_deleted=False) \
            .order_by(Post.created.desc()) \
            .paginate(pagination_parameters.page, pagination_parameters.page_size, max_per_page=20)
        return interesting_posts.items


@blog_blueprint.route("/create-post")
class CreatePost(MethodView):
    """Создание нового поста."""

    @blog_blueprint.arguments(PostArgsSchema)
    @blog_blueprint.response(201, PostSchema)
    def post(self, new_post_data: dict):
        """Добавление нового поста в блог."""
        try:
            new_post = create_new_post(**new_post_data)
            return new_post
        except PostException as error:
            abort(400, message=f"Post error: {error}.")


@blog_blueprint.route("/<post_alias>")
class PostByAlias(MethodView):
    """Работа с существующим постов в блоге по его псевдониму."""

    @blog_blueprint.response(200, PostSchema)
    def get(self, post_alias: str):
        """Вернет неудаленный пост в блоге по его псевдониму."""
        interesting_post = Post.query.filter_by(alias=post_alias, is_deleted=False).first()
        if interesting_post is None:
            abort(404, message="Post not found.")
        return interesting_post

    @blog_blueprint.arguments(PostArgsSchema)
    @blog_blueprint.response(200, PostSchema)
    def put(self, update_post_data: dict, post_alias: str):
        """Обновление существующего поста в блоге."""
        try:
            updated_post = update_post(
                old_alias=post_alias,
                new_alias=update_post_data["alias"],
                new_title=update_post_data["title"],
                new_text=update_post_data["text"],
            )
            return updated_post
        except PostException as error:
            abort(404, message=f"Post error: {error}.")

    @blog_blueprint.response(204)
    def delete(self, post_alias: str):
        """Удаление поста в блоге."""
        if not mark_post_deleted(post_alias):
            abort(404, message="Post not found.")
