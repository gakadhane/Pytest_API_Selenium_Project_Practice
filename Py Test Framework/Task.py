import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def test_amazon():
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.maximize_window()
    driver.get("https://www.amazon.in/")

@allure.title("verifiedtitle")
@pytest.mark.regression
def test_signin(test_amazon):
    element = driver.find_element("xpath", "(//span[@class='nav-icon nav-arrow'])[2]")
    a = ActionChains(driver)
    driver.find_element("xpath", "(//span[@class='nav-action-inner'])[2]").click()
    print("sign in clicked")

# @pytest.mark.regression
# def test_login(test_amazon):
#     driver.find_element("xpath", "//a[@class='ico-register']").click()
#     print("login successfully")