import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_alert():
    # Set up the WebDriver: Initialize the WebDriver for your preferred browser (e.g., Chrome).
    driver = webdriver.Chrome()

    try:
        # Open the First URL: Navigate to the first URL using the `get` method.
        driver.get('https://demo.automationtesting.in/Alerts.html')

        # Set explicit wait time (e.g., 10 seconds)
        wait = WebDriverWait(driver, 10)

        # WebDriver will wait until the element is visible or 10 seconds have passed
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@onclick='alertbox()']")))

        if element.is_displayed():
            print('Element is displayed')
        else:
            print('Element is not displayed')

        # Click the element
        element.click()

        # Switch to the alert
        alert = driver.switch_to.alert

        # Accept the alert (click OK)
        alert.accept()

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    pytest.main(["-s", "your_test_script.py"])  # Ensure -s flag is used to show print statements
