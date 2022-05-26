import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request, abort
from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

post_blueprint = Blueprint("post_blueprint", __name__, template_folder="templates")
posts_dao = PostsDAO("data/data.json")
comments_dao = CommentsDAO("data/comments.json")

logger = logging.getLogger("basic")

@post_blueprint.route("/")
def posts_all():

    logger.debug("запрошенны все посты")
    try:
        posts = posts_dao.get_all()
        return render_template("index.html", posts=posts)
    except:
        return "Something went wrong"


@post_blueprint.route("/posts/<int:post_pk>/")
def posts_one(post_pk):
    logger.debug("Запрошен один пост")
    try:
        post = posts_dao.get_post_by_pk(post_pk)
        comments = comments_dao.get_by_post_pk(post_pk)
    except (JSONDecodeError, FileNotFoundError) as error:
        return render_template("error.html", error=error)
    else:
        if post is None:
            abort(404)
        comment_count = len(comments)
        return render_template("post.html", post=post, comments=comments, comment_count=comment_count)

@post_blueprint.errorhandler(404)
def post_error(error):

    return render_template("error.html", error=error), 404

@post_blueprint.route("/search/")
def posts_search():
    s = request.args.get("s", "")
    logger.debug(f"Поиск поста по запросу: {s}")

    posts_found = posts_dao.search_for_posts(s)
    logger.debug(f"смотрим что нафильтровал: {posts_found}")
    posts_count = len(posts_found)
    return render_template("search.html", posts_found=posts_found, posts_count=posts_count)


@post_blueprint.route("/users/<user_name>/")
def posts_user(user_name):

    posts = posts_dao.get_posts_by_user(user_name)
    logger.debug(f"Переход на страницу постов: {posts}")

    return render_template("user-feed.html", posts=posts)

@post_blueprint.route("/tegstaff/")
def posts_tag():
    posts = posts_dao.search_for_hash()

    return render_template("tag.html", posts=posts)
