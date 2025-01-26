# synchronized
# Implicit wait
# Explicit wait
# Thread.sleep()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=s)
driver.implicitly_wait(5)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# clickable_element = WebDriverWait(driver, 10)
# clickable_element.until(EC.frame_to_be_available_and_switch_to_it("xpath","//input[@id='nav-search-submit-button']"))
# clickable_element.until(EC.alert_is_present)
