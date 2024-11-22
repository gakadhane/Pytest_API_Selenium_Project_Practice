import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=s)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(4)
print(driver.title)
print(driver.current_url)

driver.find_element("xpath", "//a[@class='ico-register']").click()
driver.find_element("xpath","//input[@id='gender-male']").click()
driver.find_element("name", "FirstName").send_keys("Gaurav")
driver.find_element("name", "LastName").send_keys("Kadhane")
driver.find_element("name", "Email").send_keys("test22112024novtest@yopmail.com")
driver.find_element("name", "Password").send_keys("Test@123")
driver.find_element("name", "ConfirmPassword").send_keys("Test@123")
time.sleep(2)
driver.find_element("xpath","//input[@id='register-button']").click()
time.sleep(2)
driver.find_element("name", "q").send_keys("laptop")
driver.find_element("xpath","//input[@type='submit']").click()
time.sleep(2)
driver.find_element("xpath","//input[@value='Add to cart']").click()
time.sleep(2)
driver.find_element("xpath","(//a[contains(text(),'Computers')])[3]").click()

xyz=driver.find_element("partial link text","cart")
print(xyz.text)
print(xyz.tag_name)
xyz.click()

time.sleep(4)

driver.close()