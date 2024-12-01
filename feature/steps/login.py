import time

from behave import *
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
import logging

@given(u'open browser')
def step_impl(context):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login ")
    time.sleep(4)


@when(u'enter user name "Admin" passwords "admin123"')
def step_impl(context):
    driver.find_element("name", "username").send_keys("Admin")
    driver.find_element("name", "password").send_keys("admin123")



@then(u'click login button')
def step_impl(context):
    driver.find_element("xpath", "//button[@type='submit']").click()



@then(u'Home page loaded successfully')
def step_impl(context):
    logging.info("Home page loaded successfully")