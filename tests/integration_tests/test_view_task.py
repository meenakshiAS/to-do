import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.skip
def test_view_task(chrome_browser, user, task, wait):
    # Get Homepage
    chrome_browser.get("http://127.0.0.1:8005")
    assert "Login" in chrome_browser.title

    # Login user to access user's saved tasks
    username_input = wait.until(ec.visibility_of_element_located((By.ID, "username")))
    username_input.send_keys("carl")
    time.sleep(3)

    password_input = wait.until(ec.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys("pass1234")
    time.sleep(3)

    login_button = wait.until(ec.visibility_of_element_located((By.ID, "login")))
    login_button.click()
    time.sleep(3)

    # Check if user is redirected to homepage
    header_text = wait.until(ec.visibility_of_element_located((By.TAG_NAME, "h1"))).text
    assert header_text == "Task List"
    time.sleep(3)

    # View individual task
    card_link = wait.until(
        ec.visibility_of_element_located((By.LINK_TEXT, "Brainstorming"))
    )
    card_link.click()
    time.sleep(3)

    page_heading = header_text = wait.until(
        ec.visibility_of_element_located((By.TAG_NAME, "h2"))
    ).text
    assert page_heading == "Brainstorming"
    time.sleep(20)

    # Logout user
    logout_button = wait.until(ec.visibility_of_element_located((By.ID, "logout")))
    logout_button.click()
    time.sleep(3)

    assert "Login" in chrome_browser.title
