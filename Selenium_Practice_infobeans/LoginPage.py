from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators for elements on the page
    username_field = (By.ID, "txtUsername")
    password_field = (By.ID, "txtPassword")
    login_button = (By.ID, "btnLogin")
    #error_message = (By.ID, "spanMessage")

    # Actions or Methods to interact with elements on the page
    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()


    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
