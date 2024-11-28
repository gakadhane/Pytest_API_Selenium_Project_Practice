import pytest
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

@pytest.mark.smoke
@pytest.mark.regression
def test_clickBooks(test_verifyURL):
    expected_title = "Demo Web Shop"
    actual_title = driver.title
    # Assert that the actual title matches the expected title
    assert actual_title == expected_title, f"Title mismatch: Expected '{expected_title}"
    driver.find_element("xpath","(//a[contains(text(),'Books')])[1]").click()
    assert "books" in driver.current_url.lower(), "Failed to navigate to Books page"
    expected_title = "Demo Web Shop. Books"
    actual_title = driver.title
    # Assert that the actual title matches the expected title
    assert actual_title == expected_title, f"Title mismatch: Expected '{expected_title}"