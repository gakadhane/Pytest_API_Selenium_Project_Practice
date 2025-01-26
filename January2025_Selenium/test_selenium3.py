import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@allure.title("Test Selenium GET")
def test_selenium_GET():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.quit()



