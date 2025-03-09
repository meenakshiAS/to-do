from django.urls import reverse

from pytest_django.asserts import assertRedirects


def test_register_user(client):
    response = client.get(reverse("accounts:register"))
    assert response.status_code == 200
