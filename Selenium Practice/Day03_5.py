#Action class
#drag and drop

import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=s)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(4)

#drag and drop

elementsource=driver.find_element("xpath","(//div[@id='box3'])[1]")
elementtarget=driver.find_element("xpath","//div[@id='box104']")

a=ActionChains(driver)

a.drag_and_drop(elementsource, elementtarget).perform()
