#Action class
# Move to element =mouse hover
#contex click = right click

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=s)
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
time.sleep(2)

element = driver.find_element("xpath","((//a[contains(text(),'Computers')])[1])")
a=ActionChains(driver)

# Move to element =mouse hover

a.move_to_element(element).perform()

#contex click = right click

a.context_click(element).perform()