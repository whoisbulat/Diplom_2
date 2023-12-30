import allure
import requests
from faker import Faker


fake = Faker()

class TestUpdateUser:
    @allure.title('Проверяем изменение данных пользователя с токеном авторизациии')
    def test_update_user_with_authorization(self, register_and_login_user):
        access_token = register_and_login_user
        # Изменяем информацию о пользователе
        updated_name = fake.first_name()
        updated_email = fake.email()
        updated_user_data = {
            "name": updated_name,
            "email": updated_email
        }
        update_response = requests.patch("https://stellarburgers.nomoreparties.site/api/auth/user",
                                         json=updated_user_data, headers={"authorization": access_token})
        updated_user = update_response.json()["user"]
        assert update_response.status_code == 200 and updated_user["name"] == updated_name and updated_user[
            "email"] == updated_email


    @allure.title('Проверяем изменение данных пользователя без токена авторизациии')
    def test_modify_user_without_authorization(self):
        updated_name = fake.first_name()
        updated_email = fake.email()
        updated_user_data = {
            "name": updated_name,
            "email": updated_email
        }
        update_response = requests.patch("https://stellarburgers.nomoreparties.site/api/auth/user",
                                     json=updated_user_data)
        assert update_response.status_code == 401 and "You should be authorised" in update_response.json()["message"]



