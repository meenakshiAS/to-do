from django.shortcuts import reverse


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 302


def test_create_task_view(user_client, task_form_valid):
    response = user_client.get("/create_task/")
    assert response.status_code==200
    response = user_client.post(reverse("tasks:create_task"), data=task_form_valid)
    assert response.status_code==302
