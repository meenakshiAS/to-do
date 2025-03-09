import time

from selenium.webdriver.common.by import By


def test_view_task(chrome_browser, user, task):
    # Get Homepage
    chrome_browser.get("http://127.0.0.1:8005")
    assert "Login" in chrome_browser.title

    # Login user to access user's saved tasks
    username_input = chrome_browser.find_element(By.ID, 'username')
    username_input.send_keys('carl')
    time.sleep(1)
    password_input = chrome_browser.find_element(By.ID, 'password')
    password_input.send_keys('pass1234')
    time.sleep(1)
    login_button = chrome_browser.find_element(By.ID, 'login')
    login_button.click()
    time.sleep(3)

    header_text = chrome_browser.find_element(By.TAG_NAME, 'h1').text
    assert header_text == 'Task List'































    """
    join_link = chrome_browser.find_element(By.LINK_TEXT, 'JOIN IEEE')
    join_link.click()
    header_text = chrome_browser.find_element(By.TAG_NAME, 'h1').text
    assert header_text == 'Learn About IEEE Membership'
     # type in text
    signup_link = chrome_browser.find_element(By.LINK_TEXT, 'Sign up')
    signup_link.click()
    time.sleep(5)
    first_name_input = chrome_browser.find_element(By.ID, 'FirstName')
    first_name_input.send_keys('Jane')
    time.sleep(1)
    last_name_input = chrome_browser.find_element(By.ID, 'LastName')
    last_name_input.send_keys('Doe')
    time.sleep(1)
    email_input = chrome_browser.find_element(By.CLASS_NAME, 'Email')
    email_input.send_keys('janedoe@test.com')
    time.sleep(1)
    policy_check = chrome_browser.find_element(By.LINK_TEXT, 'IEEE Privacy Policy:')
    policy_check.click()
    submit_button = chrome_browser.find_element(By.TAG_NAME, 'button')
    submit_button.click()
    time.sleep(1)
    confirmation = chrome_browser.find_element(By.TAG_NAME, 'strong').text
    assert confirmation == 'Subscription Confirmation'
    time.sleep(1)
    """
