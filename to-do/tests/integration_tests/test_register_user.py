import time
import uuid

from selenium.webdriver.common.by import By


def test_register_user(chrome_browser, user):
    # Open the register page to test
    chrome_browser.get("http://127.0.0.1:8005/accounts/register")
    assert "register" in chrome_browser.title
    # Enter Registration Details
    username_input = chrome_browser.find_element(By.ID, "username")
    username_input.send_keys("test")
    time.sleep(1)
    first_name = chrome_browser.find_element(By.ID, "first_name")
    first_name.send_keys("Test")
    time.sleep(1)
    last_name = chrome_browser.find_element(By.ID, "last_name")
    last_name.send_keys("Integration")
    time.sleep(1)
    email = chrome_browser.find_element(By.ID, "email")
    length = 8
    random_string = str(uuid.uuid4()).replace("-", "")[:length]
    email_id = random_string + "@gmail.com"
    email.send_keys(email_id)
    time.sleep(1)
    password1 = chrome_browser.find_element(By.ID, "password1")
    password1.send_keys("Test@12345678")
    time.sleep(1)
    password2 = chrome_browser.find_element(By.ID, "password2")
    password2.send_keys("Test@12345678")
    time.sleep(1)
    register_button = chrome_browser.find_element(By.ID, "register")
    register_button.click()
    time.sleep(1)
    # Check user redirected to login page
    header_text = chrome_browser.find_element(By.TAG_NAME, "h2").text
    assert header_text == "Log in"
