import time

# import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


# @pytest.mark.skip
def test_delete_task(chrome_browser, wait, user, task_2):
    """Integration test for delete task"""
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

    login_button = wait.until(ec.visibility_of_element_located((By.NAME, "login")))
    login_button.click()
    time.sleep(3)

    # Check if user is redirected to homepage
    header_text = wait.until(ec.visibility_of_element_located((By.TAG_NAME, "h1"))).text
    assert header_text == "Task List"
    time.sleep(1)

    # View individual task
    card_link = wait.until(
        ec.visibility_of_element_located((By.LINK_TEXT, "Documentation"))
    )
    card_link.click()
    time.sleep(3)

    # Delete the task
    header_text = wait.until(
        ec.visibility_of_element_located((By.LINK_TEXT, "Delete Task"))
    )
    header_text.click()
    time.sleep(3)
