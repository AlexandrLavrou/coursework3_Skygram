import json


class PostsDAO:
    """"""
    def __init__(self, path):
        self.path = path

    def _load(self):
        with open(f"{self.path}", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        """
        возвращает все посты
        """

        return self._load()

    def get_post_by_pk(self, pk):
        """
        возвращает один пост по идентификатору.
        """
        posts = self.get_all()

        for post in posts:
            if post["pk"] == pk:
                return post

    def get_posts_by_user(self, user_name):
        """
        возвращает посты определенного пользователя.
        Функция должна вызывать ошибку ValueError если такого пользователя нет
        и пустой список, если у пользователя нет постов
        """
        posts = self.get_all()

        posts_of_user = []
        for post in posts:
            if post["poster_name"] == user_name.lower():
                posts_of_user.append(post)
        return posts_of_user

    def search_for_posts(self, query):
        """
        возвращает список постов по ключевому слову
        """
        posts = self.get_all()
        posts_filtered = []
        for post in posts:
            if query.lower() in post["content"].lower():
                posts_filtered.append(post)
        return posts_filtered

    def search_for_hash(self, hash_tag):
        """
        Возвращает
        :param hash_tag:
        :return:
        """
        pass

    def get_posts_by_user(user_name):
        """возвращает посты определенного пользователя.
        Функция должна вызывать ошибку ValueError если такого пользователя нет
        и пустой список, если у пользователя нет постов"""
        pass

    def get_comments_by_post_id(post_id):
        """возвращает комментарии определенного поста.
        Функция должна вызывать ошибку ValueError если такого поста нет
        и пустой список, если у поста нет комментов. """
        pass
