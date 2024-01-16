import allure
import requests
from faker import Faker



fake = Faker()

class TestCreateOrder:
    @allure.title('Проверяем создания заказа без токена авторизации')
    def test_create_order_without_authorization(self):
        data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6f","61c0c5a71d1f82001bdaaa70","61c0c5a71d1f82001bdaaa71"]
        }
        response = requests.post(" https://stellarburgers.nomoreparties.site/api/orders", data=data)
        assert response.status_code == 200 and response.json()["success"] == True and response.json()["order"]
        print(response.json()["order"])


    @allure.title('Проверяем создание заказа с токеном авторизации')
    def test_create_order_with_authorization(self, register_and_login_user):
        access_token = register_and_login_user
        data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6f","61c0c5a71d1f82001bdaaa70","61c0c5a71d1f82001bdaaa71"]
        }
        response = requests.post("https://stellarburgers.nomoreparties.site/api/orders",
                                  data=data, headers={"Authorization": access_token})
        assert response.status_code == 200 and response.json()["order"] and response.json()["success"] == True

    @allure.title('Проверяем что вернется 500 при невалидном заказе')
    def test_update_user_with_invalid_hash_in_request_returns_500(self):

        data = {
            "ingredients": ["invalidhash"]
        }

        response = requests.post(" https://stellarburgers.nomoreparties.site/api/orders", data=data)
        assert response.status_code == 500

    @allure.title('Проверяем что вернется 400 при пустом заказе')
    def test_update_user_not_providing_any_ingredient_returns_400(self):

        data = {
            "ingredients": [""]
        }

        response = requests.post(" https://stellarburgers.nomoreparties.site/api/orders", data=data)
        assert response.status_code == 400