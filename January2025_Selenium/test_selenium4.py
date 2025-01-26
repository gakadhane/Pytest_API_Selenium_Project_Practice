import allure
from selenium import webdriver

@allure.title("Verify the title ")
def test_selenium_Chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    print(driver.title)
    assert driver.title == "Google"
    print(driver.session_id)
    print(driver.current_url)
    print(driver.page_source)
    driver.quit()

def test_selenium_Edge():
    driver = webdriver.Edge()
    driver.implicitly_wait(1)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    print(driver.title)
    assert driver.title == "Google"
    print(driver.session_id)
    print(driver.current_url)
    print(driver.page_source)
    driver.quit()