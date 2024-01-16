import allure
import pytest
import requests
from faker import Faker


fake = Faker()

class TestLoginUser:
    @allure.title('Проверяем успешный логин курьера')
    def test_success_login_user(self, register_user_get_user_credentials):
        user = register_user_get_user_credentials

        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", data=user)
        assert response.status_code == 200 and response.json()["success"] == True and "accessToken" in response.json() \
               and "refreshToken" in response.json() and  "user" in response.json() and "email" in response.json()["user"] \
               and "name" in response.json()["user"]


    @allure.title('Проверяем логин с пустым логином или паролем')
    @pytest.mark.parametrize("email, password", [
        ("test-data@yandex.ru", ""),
        ("", "password")])
    def test_create_user_without_required_fields(self, email, password):
        user = {
            "email": email,
            "password": password
        }

        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=user)
        assert response.status_code == 401 and response.json()["message"] == "email or password are incorrect" \
               and response.json()["success"] == False



