import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


@pytest.fixture()
def test_verifyURL():
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.maximize_window()
    driver.get("https://blazedemo.com/")

def test_clickflight(test_verifyURL):
    driver.find_element("xpath", "//input[@type = 'submit']").click()
    print("clicked flight finding ")

def test_chooseflight():
    driver.find_element("xpath", "(//input[@type = 'submit'])[2]").click()
    print("choose flight")

def test_firstname():
    driver.find_element("xpath", "//input[@id = 'inputName']").send_keys("Gaurav")
    driver.find_element("xpath", "//input[@name = 'address']").send_keys("banner")
    driver.find_element("xpath", "//input[@name = 'city']").send_keys("pune")
    driver.find_element("xpath", "//input[@name = 'zipCode']").send_keys("444001")
    x = driver.find_element("xpath", "//select[@name = 'cardType']")
    sel = Select(x)
    sel.select_by_index(2)
    driver.find_element("xpath", "//input[@id = 'creditCardNumber']").send_keys("5123450000000008")
    driver.find_element("xpath", "//input[@id = 'creditCardMonth']").send_keys("01")
    driver.find_element("xpath", "//input[@id = 'creditCardYear']").send_keys("2039")
    driver.find_element("xpath", "//input[@id = 'nameOnCard']").send_keys("test")
    driver.find_element("xpath", "//input[@type = 'submit']").click()