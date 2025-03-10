import time

from selenium.webdriver.common.by import By


# Integration test for delete task
def test_delete_task(chrome_browser, user, task_2):
    # Get Homepage
    chrome_browser.get("http://127.0.0.1:8005")
    assert "Login" in chrome_browser.title

    # Login user to access user's saved tasks
    username_input = chrome_browser.find_element(By.ID, "username")
    username_input.send_keys("carl")
    time.sleep(1)
    password_input = chrome_browser.find_element(By.ID, "password")
    password_input.send_keys("pass1234")
    time.sleep(1)
    login_button = chrome_browser.find_element(By.ID, "login")
    login_button.click()
    time.sleep(1)

    # Check if user is redirected to homepage
    header_text = chrome_browser.find_element(By.TAG_NAME, "h1").text
    assert header_text == "Task List"

    # View individual task
    card_link = chrome_browser.find_element(By.LINK_TEXT, "Documentation")
    card_link.click()
    time.sleep(1)
    # Delete the task
    header_text = chrome_browser.find_element(By.LINK_TEXT, "Delete Task")
    header_text.click()
    time.sleep(1)

    # Logout user
    logout_button = chrome_browser.find_element(By.ID, "logout")
    logout_button.click()
    time.sleep(1)
    assert "Login" in chrome_browser.title
