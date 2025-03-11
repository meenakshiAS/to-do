import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Integration test for delete task
def test_delete_task(chrome_browser, wait, user, task_2):
    # Get Homepage
    chrome_browser.get("http://127.0.0.1:8005")
    assert "Login" in chrome_browser.title

    # Login user to access user's saved tasks
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    username_input.send_keys("carl")
  
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys("pass1234")
   
    login_button = wait.until(EC.visibility_of_element_located((By.ID, "login")))
    login_button.click()

    # Check if user is redirected to homepage
    header_text = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text
    assert header_text == "Task List"

    # View individual task
    card_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Documentation")))
    card_link.click()
   
    # Delete the task
    header_text = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Delete Task")))
    header_text.click()
    time.sleep(1)

    # Logout user
    logout_button = wait.until(EC.visibility_of_element_located((By.ID, "logout")))
    logout_button.click()
    assert "Login" in chrome_browser.title
