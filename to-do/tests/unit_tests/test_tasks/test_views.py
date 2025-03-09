from pytest_django.asserts import assertRedirects


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 302
    assertRedirects(response, "/accounts/login/?next=/")
