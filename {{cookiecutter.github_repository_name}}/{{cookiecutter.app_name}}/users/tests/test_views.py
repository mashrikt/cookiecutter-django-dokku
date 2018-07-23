import pytest
import factory
from django.urls import reverse

from .factories import fake, User, UserFactory


class TestRegistration:
    url = reverse("v1:users:rest_register")
    test_password = "test_pass"

    @pytest.fixture
    def register_data(self):
        data = {
            'email': fake.email(),
            {%- if cookiecutter.email_user.lower() == "n" %}
            'username': fake.first_name(),
            {%- endif %}
            'password1': self.test_password,
            'password2': self.test_password,
        }
        return data

    def test_user_registration_success(self, client, register_data, db):
        request = client.post(self.url, register_data)

        {%- if cookiecutter.email_user.lower() == "n" %}
        user = User.objects.filter(id=request.data["user"]["pk"], is_active=True)
        {%- else %}
        user = User.objects.filter(id=request.data["user"]["id"], is_active=True)
        {%- endif %}


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
    password = "test_pass"

    def test_login(self, user, client):

        assert user.check_password(self.password)

        data = {
            {%- if cookiecutter.email_user.lower() == "n" %}
            "username": user.username,
            {%- else %}
            "email": user.email,
            {%- endif %}
            "password": self.password
        }

        request = client.post(self.url, data)

        assert request.status_code == 200
        assert request.data["user"]["email"] in user.email

    {%- if cookiecutter.email_user.lower() == "n" %}

    def test_wrong_username_login(self, user, client, db):

        data = {
            "username": fake.first_name(),
            "password": self.password
        }

        request = client.post(self.url, data)

        assert request.status_code == 400

    {%- else %}

    def test_wrong_email_login(self, user, client):

        data = {
            "email": fake.email(),
            "password": self.password
        }

        request = client.post(self.url, data)

        assert request.status_code == 404

    {%- endif %}

    def test_wrong_password_login(self, user, client):

        data = {
            {%- if cookiecutter.email_user.lower() == "n" %}
            "username": user.username,
            {%- else %}
            "email": user.email,
            {%- endif %}
            "password": fake.word()
        }

        request = client.post(self.url, data)

        assert request.status_code == 400


class TestLogout:

    url = reverse("v1:users:rest_logout")

    def test_logout(self, auth_client):

        request = auth_client.post(self.url)

        assert request.status_code == 200
