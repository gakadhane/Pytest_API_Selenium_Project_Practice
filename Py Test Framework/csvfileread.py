import time
import pytest
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# Fixture to set up WebDriver
@pytest.fixture(scope="function")
def driver1():
    # Set up WebDriver
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.maximize_window()



# Function to fetch test data from the specified CSV file
def get_csv_data(file_path):
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]  # Returns a list of dictionaries


# Test using data from CSV
def test_example(driver1):
    # Specify the path to your CSV file
    csv_file_path = r"C:\gaurav\selenium\books.csv"

    # Fetch test data from the CSV file
    test_data_list = get_csv_data(csv_file_path)

    for test_data in test_data_list:
        url = test_data["url"]
        username = test_data["username"]
        password = test_data["password"]

        # Open the URL
        driver.get(url)
        time.sleep(2)

        # Test steps
        driver.find_element("name", "username").send_keys(username)
        driver.find_element("name", "password").send_keys(password)


        # Navigate back to reset for the next test case
        driver.back()
        time.sleep(2)


