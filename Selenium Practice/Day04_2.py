
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=s)
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")

driver.maximize_window()
print(driver.title)
print(driver.current_url)

# driver.find_element("name", "username").send_keys("Admin")
# driver.find_element("name", "password").send_keys("admin123")
driver.find_element("xpath", "//input[@type= 'text']").click()
driver.find_element("id", "twotabsearchtextbox").send_keys("iphone")
driver.find_element("xpath","//input[@id='nav-search-submit-button']").click()


driver.save_screenshot("C:\\gaurav\\gaurav.png")

# driver.execute_script("window.scrollby(0, 1000);")
# driver.execute_script("window,scrollby(0, -1000);")


ele = driver.find_element(By.XPATH, "(//span[@class='a-size-medium a-color-base a-text-normal'])[4]")
# driver.execute_script("window.scrollBy(0, ele)")
driver.execute_script("arguments[0].scrollIntoView();", ele)