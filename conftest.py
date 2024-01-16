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
    requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=new_user)

    login_credentials = {
        "email": email,
        "password": password
    }
    login_response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=login_credentials)
    access_token = login_response.json()["accessToken"]

    yield access_token


@pytest.fixture
def user_with_create_order(register_and_login_user):
    access_token = register_and_login_user
    data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa71"]
    }
    response = requests.post("https://stellarburgers.nomoreparties.site/api/orders",
                             data=data, headers={"Authorization": access_token})

    return response.json()['number']


@pytest.fixture
def register_user_get_user_credentials():
    email = fake.email()
    password = fake.password()
    name = fake.first_name()

    new_user = {
        "email": email,
        "password": password,
        "name": name
    }
    requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=new_user)


