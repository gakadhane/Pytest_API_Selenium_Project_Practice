import pytest
from selenium import webdriver

from LoginPage import LoginPage


@pytest.fixture(scope="module")
def setup():
    # Set up WebDriver (Chrome in this case)
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')  # Specify path to chromedriver
    driver.get("https://opensource-demo.orangehrmlive.com/")  # URL for OrangeHRM login page
    yield driver  # This allows us to use the driver in the tests
    driver.quit()  # Close the browser after the tests are done


def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_button()
    # Perform valid login
    login_page.login("Admin", "admin123")