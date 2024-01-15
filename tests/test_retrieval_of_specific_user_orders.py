import allure
import requests
from faker import Faker




fake = Faker()

class TestRetrievalOfCpecificUserOrder:
    @allure.title('Проверяем падение ошибки 401 при получение заказа конкретного пользователя без токена авторизации')
    def test_retrieval_user_orders_with_authorization(self):

        response = requests.get("https://stellarburgers.nomoreparties.site/api/orders")

        assert response.status_code == 401 and response.json()["success"] == False and \
               response.json()["message"] == "You should be authorised"

    @allure.title('Проверяем получение заказа конкретного пользователя c токеном авторизацией')
    def test_retrieval(self, user_with_create_order):
        access_token = user_with_create_order

        response = requests.get("https://stellarburgers.nomoreparties.site/api/orders", headers={"authorization": access_token})

        ingredient_in_order = ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa71"]

        assert response.status_code == 200 and response.json()["success"] == True and \
               response.json()["orders"][0]["ingredients"] == ingredient_in_order










