from django.urls import reverse


# Test Register user view
def test_register_user(client):
    response = client.get(reverse("accounts:register"))
    assert response.status_code == 200
