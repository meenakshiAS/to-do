import tempfile

import pytest
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from tasks.models import Task


# Fixture for webdriver
@pytest.fixture
def driver():
    # Setup
    options = Options()
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    # Teardown
    return driver


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 100)


@pytest.fixture
def chrome_browser(driver, live_server, transactional_db):
    driver.server_url = live_server.url
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Fixture to create user
@pytest.fixture
def user(db):
    """Fixture to create a user."""
    # Setup
    user = User.objects.create_user(
        username="carl",
        email="carl@test.com",
        first_name="Carl",
        last_name="Doe",
        password="pass1234",
    )
    # Teardown
    yield user


# Fixture for logged in user
@pytest.fixture
def user_client(client, user):
    # Setup
    client.force_login(user)
    # Teardown
    yield client


# Fixture to create task 1
@pytest.fixture
def task(db, user):
    # Setup
    task = Task.objects.create(
        user=user,
        title="Brainstorming",
        description="A to do app.",
        due_date="2025-03-01",
        completed=False,
    )
    # Teardown
    yield task


# Fixture to create task 2
@pytest.fixture
def task_2(db, user):
    # Setup
    task = Task.objects.create(
        user=user,
        title="Documentation",
        description="Documentation for a to do app.",
        due_date="2025-03-01",
        completed=False,
    )
    # Teardown
    yield task


# Fixture for create task valid form
@pytest.fixture
def task_form_valid(db, user):
    # Setup
    data = {
        "user": user.id,
        "title": "Brainstorming",
        "description": "A to do app.",
        "due_date": "2025-03-01",
        "completed": False,
    }
    # Teardown
    yield data


# Fixture to register a user with valid data
@pytest.fixture
def register_user_valid(db):
    """Fixture for registering a user"""
    # Setup
    form = {
        "username": "Jane",
        "email": "jane@gmail.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "password1": "abc",
        "password2": "abc",
    }
    # Teardown
    yield form


# Fixture to register a user with invalid data: mismatch password
@pytest.fixture
def register_user_invalid(db):
    """Fixture for registering a user"""
    # Setup
    form = {
        "username": "Jane",
        "email": "jane@gmail.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "password1": "abc",
        "password2": "",
    }
    # Teardown
    yield form
