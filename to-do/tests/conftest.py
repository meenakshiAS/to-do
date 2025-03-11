import os
import tempfile
import pytest

from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 


from tasks.models import Task


@pytest.fixture
def driver():
    options = Options()
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f'--user-data-dir={user_data_dir}')
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 30)


@pytest.fixture
def chrome_browser(driver, live_server, transactional_db):
    driver.server_url = live_server.url
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def user(db):
    """Fixture to create a user."""
    user = User.objects.create_user(
        username="carl",
        email="carl@test.com",
        first_name="Carl",
        last_name="Doe",
        password="pass1234",
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
        completed=False,
    )
    return task


@pytest.fixture
def task_2(db, user):
    task = Task.objects.create(
        user=user,
        title="Documentation",
        description="Documentation for a to do app.",
        due_date="2025-03-01",
        completed=False,
    )
    return task


@pytest.fixture
def task_form_valid(db, user):
    return {
        "user": user.id,
        "title": "Brainstorming",
        "description": "A to do app.",
        "due_date": "2025-03-01",
        "completed": False,
    }


@pytest.fixture
def register_user_valid(db):
    """Fixture for registering a user"""
    form = {
        "username": "Jane",
        "email": "jane@gmail.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "password1": "abc",
        "password2": "abc",
    }
    return form
