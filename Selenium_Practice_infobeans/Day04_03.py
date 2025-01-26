# https://the-internet.herokuapp.com/frames


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=s)
# driver.get("https://the-internet.herokuapp.com/frames")
driver.maximize_window()
time.sleep(4)
driver.get("fhttps://the-internet.herokuapp.com/nested_frames")

driver.find_element("id","fn").send_keys("Plabani")
driver.switch_to.frame("frm")
driver.find_element("id","mn").send_keys("M")
driver.switch_to.default_content()
#driver.switch_to.parent_frame()
driver.find_element("id","ln").send_keys("n")

