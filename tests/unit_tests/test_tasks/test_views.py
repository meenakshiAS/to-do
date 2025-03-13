from django.shortcuts import reverse
from pytest_django.asserts import assertRedirects


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 302
    assertRedirects(response, "/accounts/login/?next=/")


def test_create_task_view(user_client, task_form_valid):
    response = user_client.get("/create_task/")
    assert response.status_code == 200
    response = user_client.post(reverse("tasks:create_task"), data=task_form_valid)
    assert response.status_code == 302


def test_delete_task(user_client, task_2):
    response = user_client.get(reverse("tasks:delete_task", args=(task_2.id,)))
    assert response.status_code == 302


def test_update_task_get(user_client, task_2):
    response = user_client.get(reverse("tasks:update_task", args=(task_2.id,)))
    assert response.status_code == 200


def test_update_task_post(user_client, task_2, task_form_valid):
    response = user_client.post(
        reverse("tasks:update_task", args=(task_2.id,)), data=task_form_valid
    )
    assert response.status_code == 302
