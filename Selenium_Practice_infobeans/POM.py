# base_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        """Wait for the element to be present and return it."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Wait for the element to be clickable and return it."""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        """Click on the element found by the locator."""
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()

    def input_text(self, locator, text):
        """Enter the given text in the field found by the locator."""
        element = self.wait_for_element(locator)
        element.send_keys(text)

    def get_text(self, locator):
        """Get the text from the element found by the locator."""
        element = self.wait_for_element(locator)
        return element.text

    def is_element_present(self, locator):
        """Check if the element is present on the page."""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

#
# -----------------------------------------------------------
# login_page.py
# from selenium.webdriver.common.by import By
# from base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators for login elements
    username_field = (By.ID, "txtUsername")
    password_field = (By.ID, "txtPassword")
    login_button = (By.ID, "btnLogin")
    error_message = (By.ID, "spanMessage")

    # Actions specific to the login page
    def enter_username(self, username):
        self.input_text(self.username_field, username)

    def enter_password(self, password):
        self.input_text(self.password_field, password)

    def click_login_button(self):
        self.click_element(self.login_button)

    def get_error_message(self):
        return self.get_text(self.error_message)

    def login(self, username, password):
        """Performs login action using provided username and password."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()


# -----------------------
# test_login.py
# import pytest
# from login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)

    # Perform valid login
    login_page.login("Admin", "admin123")

    # Assert that the dashboard page is loaded after login
    assert "Dashboard" in driver.title


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    # Perform invalid login
    login_page.login("InvalidUser", "InvalidPassword")

    # Assert that an error message is displayed
    assert login_page.get_error_message() == "Invalid credentials"


