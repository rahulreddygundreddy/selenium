from selenium import webdriver
from selenium.webdriver.common.by import By

drivers = webdriver.Chrome()
driver.get("https://www.croma.com")
driver.minimize_window()

print("page title is: ", driver.title)
driver.quit()
