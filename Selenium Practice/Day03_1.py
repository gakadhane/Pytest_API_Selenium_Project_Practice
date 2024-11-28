# select drop down with index and value and visible text
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=s)
driver.implicitly_wait(4)
driver.get("https://demowebshop.tricentis.com/books")
driver.maximize_window()

# driver.find_element("partial link text", "books']").click()

x = driver.find_element("xpath", "//select [@id='products-orderby']")
sel = Select(x)

sel.select_by_index(4)
# sel.select_by_index(0)
# sel.select_by_value("https://demowebshop.tricentis.com/books?orderby=6")
# sel.select_by_visible_text("Created on")