import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.get("https://www.amazon.in")
    driver.maximize_window()
    time.sleep(4)
    print(driver.title)
    print(driver.current_url)
    yield driver
    driver.quit()

def test_login(setup):
    driver = setup
    driver.find_element(By.ID, "nav-link-accountList").click()
    driver.find_element(By.ID, "ap_email").send_keys("gkadhane@gmail.com")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "ap_password").send_keys("Garun0d@y")
    driver.find_element(By.ID, "signInSubmit").click()

def test_search_product(setup):
    driver = setup
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("TV")
    search_box.submit()

def test_add_to_cart(setup):
    driver = setup
    driver.find_element("xpath", "(//button[@class='a-button-text'])[1]").click()
    driver.find_element("xpath", "//span[@id='nav-cart-count']").click()

def test_buy_now(setup):
    driver = setup
    driver.find_element("xpath", "//input[@name='proceedToRetailCheckout']").click()

def test_use_address(setup):
    driver = setup
    driver.find_element("xpath", "(//input[@class='a-button-input'])[2]").click()
    time.sleep(2)

def test_add_card_information(setup):
    driver = setup
    driver.find_element(By.NAME, "cardnumber").send_keys("4512345000000008")
    driver.find_element(By.NAME, "expiry").send_keys("01/39")
    driver.find_element(By.NAME, "cvv").send_keys("100")

def test_click_payment(setup):
    driver = setup
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
