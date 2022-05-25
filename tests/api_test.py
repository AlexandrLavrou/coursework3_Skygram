from main import app


class TestAPI:

    def test_app_all_posts_status_code(self):
        """Проверяем получение корректного списка"""
        response = app.test_client().get("/api/posts", follow_redirects=True)

        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_app_one_post_status_code(self):
        """Проверяем получение корректного списка"""
        response = app.test_client().get("/api/posts/1", follow_redirects=True)

        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"