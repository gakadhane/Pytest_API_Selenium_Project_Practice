import allure
from selenium.webdriver.chrome import webdriver

@allure.title("Test Selenium GET")
def test_selenium_GET():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.quit()
