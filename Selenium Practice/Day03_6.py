#Alert
from selenium.webdriver.common.alert import Alert
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\gaurav\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=s)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
time.sleep(2)

a=ActionChains(driver)
element = driver.find_element("xpath","//button[text()='Double-Click Me To See Alert']")

# Double click
a.double_click(element).perform()

#Alert pop up text
alert=Alert(driver)
time.sleep(2)

print(alert.text)
alert.accept()
# alert.dismiss()

# WebElement element1=driver.findElement(By.xpath("//button[text()='Double-Click Me To See Alert']"));
# Actions act=new Actions(driver);
# act.doubleClick(element1).perform();
# Alert a=driver.switchTo().alert();
# System.out.println(a.getText());