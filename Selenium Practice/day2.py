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

xyz=driver.find_element("partial link text","Register")
print(xyz.text)
print(xyz.tag_name)
xyz.click()


driver.close()