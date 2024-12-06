from BasePagePOM import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "loginButton")

    def login(self, username, password):
        self.input_text(self.username_field, username)
        self.input_text(self.password_field, password)
        self.click_element(self.login_button)