import pytest
from django.urls import reverse

from {{cookiecutter.app_name}}.users.tests import fake, User, UserFactory


class TestRegistration:
    url = reverse("api:auth:rest_register")
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
