from selenium import webdriver
import time


def main_window():
    # Set up the WebDriver: Initialize the WebDriver for your preferred browser (e.g., Chrome).

    driver = webdriver.Chrome()

    # Open the First URL: Navigate to the first URL using the `get` method.
    driver.get('https://demo.automationtesting.in/Windows.html')

    # Get the Current Window Handle: Store the handle of the current window (main window) using `current_window_handle`.(the first tab)
    main_window_handle = driver.current_window_handle
    print(main_window_handle)

    # Open a New Tab: Use `execute_script` to open a new tab with a specified URL.
    driver.execute_script("window.open('http://google.com', '_blank');")

    # Get All Window Handles: Retrieve a list of all window handles using the `window_handles` property.
    window_handles = driver.window_handles
    print(window_handles)

    # Switch to the New Tab: Use `switch_to.window` to switch to the new tab by referencing its handle.(the second tab)
    driver.switch_to.window(window_handles[1])
    time.sleep(5)

    # Switch Back to the Main Window: Switch back to the original window using its handle.(the first tab)
    driver.switch_to.window(main_window_handle)

    time.sleep(5)
    # Perform Actions in the Main Window: Continue performing actions in the main window as needed.
    print(driver.title)

    # Close the Browser: Close the browser using the `quit` method.
    driver.quit()


window = main_window()
