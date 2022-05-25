import pytest

from app.posts.dao.posts_dao import PostsDAO


class TestPostDao:

    @pytest.fixture()
    def posts_dao(self):
        return PostsDAO("data/data.json")

    @pytest.fixture()
    def keys_expected(self):
        return {
            "poster_name",
            "poster_avatar",
            "pic", "content",
            "views_count",
            "likes_count",
            "pk"
        }

    def test_get_all_check_type(self, posts_dao):
        posts = posts_dao.get_all()
        assert type(posts) == list, "Ошибка типа, посты должны быть списком"
        assert type(posts[0]) == dict, "Ошибка типа, отдельный пост должен быть словарем"

    def test_get_all_has_keys(self, posts_dao, keys_expected):
        posts = posts_dao.get_all()
        for post in posts:
            post_keys = post.keys()
            assert set(post_keys) == keys_expected, "Ошибка получения ключей"

    def test_get_one_check_type(self, posts_dao):
        post = posts_dao.get_post_by_pk(1)
        assert type(post) == dict, "Ошибка пост должен быть словарем"

    def test_get_one_check_type_keys(self, posts_dao, keys_expected):
        post = posts_dao.get_post_by_pk(1)
        post_keys = post.keys()
        assert set(post_keys) == keys_expected, "Ошибка получения ключей"

    parameters_to_check_get_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]

    @pytest.mark.parametrize("post_pk", parameters_to_check_get_by_pk)
    def test_get_by_pk_correct_pk(self, posts_dao, post_pk):
        post = posts_dao.get_post_by_pk(post_pk)
        assert post["pk"] == post_pk, "Номер поста не соответствует запрашиваемому"

    parameters_to_check_get_posts_by_user = [
        ("leo", {1, 5}),
        ("johnny", {2, 6}),
        ("hank", {3, 7})
    ]

    @pytest.mark.parametrize("poster_name, post_pks_correct", parameters_to_check_get_posts_by_user)
    def test_get_posts_by_user(self, posts_dao, poster_name, post_pks_correct):
        posts = posts_dao.get_posts_by_user(poster_name)
        post_pks = set()
        for post in posts:
            post_pks.add(post["pk"])

        assert post_pks == post_pks_correct

    parameters_search_for_posts = [
        ("лампочка", {6}),
        ("Пурр", {5}),
        ("странного", {2})
    ]

    @pytest.mark.parametrize("query, post_pks_correct", parameters_search_for_posts)
    def test_search_for_posts(self, posts_dao, query, post_pks_correct):
        posts = posts_dao.search_for_posts(query)
        post_pks = set()
        for post in posts:
            post_pks.add(post["pk"])

        assert post_pks == post_pks_correct
