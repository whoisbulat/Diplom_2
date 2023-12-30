import pytest
import requests
from faker import Faker

fake = Faker()

@pytest.fixture
def register_and_login_user():
    email = fake.email()
    password = fake.password()
    name = fake.first_name()

    new_user = {
        "email": email,
        "password": password,
        "name": name
    }
    register_response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=new_user)
    if register_response.status_code != 200:
        raise Exception("Регистрация пользователя не удалась")

    login_credentials = {
        "email": email,
        "password": password
    }
    login_response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=login_credentials)
    if login_response.status_code != 200:
        raise Exception("Вход пользователя не удался")

    access_token = login_response.json()["accessToken"]

    yield access_token

    # delete_response = requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user",
    #                                   headers={"Authorization": access_token})
    # if delete_response.status_code != 200:
    #     raise Exception("Удаление пользователя не удалось")



@pytest.fixture
def user_with_create_order(register_and_login_user):
    access_token = register_and_login_user
    data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa71"]
    }
    response = requests.post("https://stellarburgers.nomoreparties.site/api/orders",
                             data=data, headers={"Authorization": access_token})

    return access_token

