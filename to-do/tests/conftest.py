import pytest
from django.contrib.auth.models import User
from django.test import Client

from tasks.models import Task


@pytest.fixture
def client(db):
    client = Client()
    return client


@pytest.fixture
def user(db):
    """Fixture to create a user."""
    user = User.objects.create_user(
        username="carl",
        email="carl@test.com",
        first_name="Carl",
        last_name="Doe",
        password="pass1234"
    )
    return user


@pytest.fixture
def user_client(client, user):
    client.force_login(user)
    return client


@pytest.fixture
def task(db, user):
    task = Task.objects.create(
        user=user,
        title="Brainstorming",
        description="A to do app.",
        due_date="2025-03-01",
        completed=False

    )
    return task


@pytest.fixture
def task_form_valid(db, user):
    return {
        "user": user.id,
        "title":"Brainstorming",
        "description": "A to do app.",
        "due_date": "2025-03-01",
        "completed": False
    }