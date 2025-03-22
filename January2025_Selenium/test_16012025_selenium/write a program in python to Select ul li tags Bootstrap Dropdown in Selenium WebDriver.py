from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the target webpage with the Bootstrap dropdown
driver.get("https://example.com")

# Wait for the dropdown button to be clickable
wait = WebDriverWait(driver, 10)
dropdown_button = wait.until(EC.element_to_be_clickable((By.ID, "dropdownMenuButton")))

# Click the dropdown button to open the menu
dropdown_button.click()

# Find all <li> elements in the dropdown menu using their CSS Selector
list_items = driver.find_elements(By.CSS_SELECTOR, "ul.dropdown-menu > li")

# Extract text from each <li> element and store it in a list
list_text = [item.text for item in list_items]

# Print each item's text
print("Dropdown Items:")
for text in list_text:
    print(text)

# Example: You can also click an item based on its text
desired_text = "Option 2"  # Change this to match your desired item
for item in list_items:
    if item.text == desired_text:
        item.click()
        break

# Close the browser
driver.quit()