import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# ✅ Test case: Open a webpage
def test_open_google():
    driver = webdriver.Chrome()  # opens Chrome browser
    driver.get("https://www.google.com")

    # Check if page title contains "Google"
    assert "Google" in driver.title

    driver.quit()  # close browser
