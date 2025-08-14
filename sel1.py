from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://www.croma.com")
# driver.maximize_window()

# print("page title is: ", driver.title)
# driver.quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://www.example.com")
# elem = driver.find_element(By.ID, "username")
# elem.send_keys("neson")
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/jsref/met_win_open.asp")
# driver.implicitly_wait(10)  # Wait for elements to load
# wait = WebDriverWait(driver,10)
# element - wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
# driver.quit()
# driver.switch_to.frame("iframeResult")  # Switch to the iframe
# print(driver.find_element(By.TAG_NAME, "h1").text)
# driver.switch_to.default_content()  # Print the text of the h1 element
# driver.quit()  # Close the browser
# driver.execute_script("window.open('https://bing.com')")
# windows = driver.window_handles
# driver.switch_to.window(windows[1])  # Switch to the new window
# print(driver.title)
# driver.switch_to.window(windows[0])  # Switch back to the original window
# driver.quit()
# action = ActionChains(driver)
# right_click_btn = driver.find_element(By.CSS_SELECTOR, ".context-menu-one")
# action.context_click(right_click_btn).perform()  # Perform right-click action
# driver.quit()
# driver.save_screenshot("amazon_screenshot.png")  # Save a screenshot
# driver.quit()  # Close the browser
driver.execute_script("window.open('https://google.com');")  # Scroll to the bottom of the page
windows = driver.window_handles
print(windows)
driver.switch_to.window(windows[1])
print("now at:", driver.title)
driver.quit()
