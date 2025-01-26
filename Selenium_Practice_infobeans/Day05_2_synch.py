# Try and Catch block

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=s)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(4)
print(driver.title)
print(driver.current_url)

driver.find_element("name", "username").send_keys("Admin")
driver.find_element("name", "password").send_keys("admin123")
driver.find_element("xpath", "//button[@type='submit']").click()

clickable_element = WebDriverWait(driver, 10)
# clickable_element.until(EC.frame_to_be_available_and_switch_to_it("xpath","//button[@type='submit']"))
# clickable_element.until(EC.alert_is_present)


try:
    clickable_element.until(EC.title_contains("OrangeRM"))
    print("Action Completed")
except:
    print("Action not Completed")
finally:
    print("title process completed")



#driver.find_element("id","mn").send_keys("M")
#driver.switch_to.default_content()

#driver.switch_to.parent_frame()
#driver.find_element("id","ln").send_keys("n")

driver.close()