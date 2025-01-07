import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def test_verifyURL():
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")

@allure.title("verifiedtitle")
@pytest.mark.smoke
@pytest.mark.regression
def test_clickBooks(test_verifyURL):
    expected_title = "Demo Web Shop"
    actual_title = driver.title
    # Assert that the actual title matches the expected title
    assert actual_title == expected_title, f"Title mismatch: Expected '{expected_title}"
    driver.find_element("xpath", "(//a[contains(text(),'Books')])[1]").click()
    print("clicked Book")
    assert "books" in driver.current_url.lower(), "Failed to navigate to Books page"

@pytest.mark.regression
@pytest.mark.computer
def test_computer(test_verifyURL):
    driver.find_element("xpath", "(//a[contains(text(),'Computers')])[3]").click()
    print("clicked Computer")

@pytest.mark.regression
@pytest.mark.login
def test_login(test_verifyURL):
    driver.find_element("xpath", "//a[@class='ico-register']").click()
    print("login successfully")


@pytest.mark.skip("skipping")
def test_clicklogout():
    print("this is just sample one")

# @pytest.fixture()
# def test_clicklogout(test_verifyURL):
#     print("this is just sample one")
