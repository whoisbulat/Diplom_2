import allure
import pytest
import requests
from faker import Faker



fake = Faker()

class TestCreateUser:
    @allure.title('Проверяем успешную регистрацию пользователя')
    def test_success_create_new_user(self):
        new_user = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.first_name()
        }
        response = requests.post(" https://stellarburgers.nomoreparties.site/api/auth/register", data=new_user)
        assert response.status_code == 200 and response.json()["success"] == True and "accessToken" in response.json() \
               and "refreshToken" in response.json() and  "user" in response.json() and "email" in response.json()["user"] \
               and "name" in response.json()["user"]



    @allure.title('Проверяем что упадет ошибка при попытки создания пользователя без обязательного поля')
    @pytest.mark.parametrize("email, password, name", [
        ("", "password","name"),
        ("email", "","name"),
        ("email", "password","")])
    def test_create_user_without_required_fields(self, email, password,name):
        user = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=user)
        assert response.status_code == 403 and response.json()["message"] == "Email, password and name are required fields" \
               and response.json()["success"] == False


    @allure.title('Проверяем что упадет ошибка при попытки создания пользователя который уже есть в системе')
    def test_check_create_identical_user(self, register_user_get_user_credentials):
        user = register_user_get_user_credentials

        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=user)

        assert response.status_code == 403 and response.json()["message"] == "User already exists" \
               and response.json()["success"] == False
