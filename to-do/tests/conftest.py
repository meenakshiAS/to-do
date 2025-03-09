import pytest
from django.contrib.auth.models import User
from selenium import webdriver

from tasks.models import Task


@pytest.fixture
def chrome_browser(live_server, transactional_db):
    driver = webdriver.Chrome()
    driver.server_url = live_server.url
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def user(db):
    """Fixture to create an admin user."""
    user = User.objects.create_user(
        username="carl",
        email="carl@test.com",
        first_name="Carl",
        last_name="Doe",
        password="pass1234"
    )
    return user


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
