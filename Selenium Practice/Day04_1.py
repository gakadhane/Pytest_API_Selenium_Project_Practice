from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=s)
driver.get("https://demowebshop.tricentis.com/books")
driver.save_screenshot("C:\\gaurav\\gaurav.png")

driver.execute_script("window.scrollby(0, 1000);")
driver.execute_script("window,scrollby(0, -1000);")
