import pytest
import factory
from django.urls import reverse

from {{cookiecutter.app_name}}.users.tests import fake, User, UserFactory


class TestRegistration:
    url = reverse("v1:users:rest_register")
    test_password = "test_pass"

    @pytest.fixture
    def register_data(self):
        data = {
            'email': fake.email(),
            'password1': self.test_password,
            'password2': self.test_password,
        }
        return data

    def test_user_registration_success(self, client, register_data, db):
        request = client.post(self.url, register_data)

        user = User.objects.filter(id=request.data["user"]["id"], is_active=True)

        assert request.status_code == 201
        assert user.exists()
        assert user[0].check_password(self.test_password)

    def test_password_mismatch(self, client, register_data, db):
        register_data["password2"] = fake.word()

        request = client.post(self.url, register_data)

        assert request.status_code == 400

    def test_unique_email(self, client, register_data, db):
        UserFactory(email=register_data["email"])

        request = client.post(self.url, register_data)

        assert request.status_code == 400


class TestLogin:

    url = reverse("v1:users:rest_login")
    email = fake.email()
    password = "test_pass"

    @pytest.fixture
    def login_user(self, user):
        user.email = self.email
        user.set_password(self.password)
        user.save()

        return user

    def test_login(self, login_user, client):

        assert login_user.check_password(self.password)

        data = {
            "email": self.email,
            "password": self.password
        }

        request = client.post(self.url, data)

        assert request.status_code == 200
        assert request.data["user"]["email"] in self.email

    def test_wrong_email_login(self, client, db):

        data = {
            "email": fake.email(),
            "password": self.password
        }

        request = client.post(self.url, data)

        assert request.status_code == 404

    def test_wrong_password_login(self, login_user, client):

        data = {
            "email": login_user.email,
            "password": fake.word()
        }

        request = client.post(self.url, data)

        assert request.status_code == 400


class TestLogout:

    url = reverse("v1:users:rest_logout")

    def test_logout(self, auth_client):

        request = auth_client.post(self.url)

        assert request.status_code == 200
