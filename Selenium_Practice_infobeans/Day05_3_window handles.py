# Get all window handles


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=s)
driver.implicitly_wait(5)
driver.get("https://toolsqa.com/")
driver.maximize_window()

driver.find_element("xpath", "(//a[@target='_blank'])[1]").click()

main_window_handle = driver.current_window_handle

# Get all window handles (including the main window and the new tab)
all_window_handles = driver.window_handles

if len(all_window_handles) > 1:
    # Find the handle of the new tab (exclude the main window handle)
    new_tab_handle = [handle for handle in all_window_handles if handle != main_window_handle][0]

    # Switch to the new tab
    driver.switch_to.window(new_tab_handle)
    print(driver.title)

driver.switch_to.window(main_window_handle)
print(driver.title)

# driver.find_element("xpath", "((//div[@class='card mt-4 top-card'])[4]").click()


driver.quit()