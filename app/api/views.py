import logging

from flask import Blueprint, request, jsonify


from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

api_blueprint = Blueprint("api_blueprint", __name__, template_folder="templates")

posts_dao = PostsDAO("data/data.json")
comments_dao = CommentsDAO("data/comments.json")

logger = logging.getLogger("basic")

@api_blueprint.route("/api/posts/")
def posts_all():
    logger.debug("Запрошены все посты через API")
    posts = posts_dao.get_all()
    return jsonify(posts)


@api_blueprint.route("/api/<int:post_pk>/")
def posts_by_pk(post_pk):
    logger.debug(f"Запрошен post по {post_pk} через API")
    posts = posts_dao.get_post_by_pk(post_pk)
    return jsonify(posts)


