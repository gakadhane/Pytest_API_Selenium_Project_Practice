import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


@pytest.fixture()
def test_verifyURL():
    # Set up WebDriver
    global driver1
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver1 = webdriver.Chrome(options=options, service=service)
    driver1.maximize_window()
    driver1.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login ")
    time.sleep(4)

# Parameterize test with different usernames and passwords
@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin", "admin123"),       # Valid credentials
        ("invalid_user", "admin123"), # Invalid username
        ("Admin", "wrongpassword"),  # Invalid password
        ("", ""),                    # Empty credentials
    ]
)


def test_login(test_verifyURL, username, password):
    # Locate and interact with username field
    username_field = driver1.find_element("name", "username")
    username_field.send_keys(username)

    # Locate and interact with password field
    password_field = driver1.find_element("name", "password")
    #password_field.clear()
    password_field.send_keys(password)

    # Click login button
    login_button = driver1.find_element("xpath", "//button[@type='submit']")
    login_button.click()