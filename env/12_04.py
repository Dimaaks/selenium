from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements('[type="text"]')
    elements.send_keys('везде 100')
finally:
    time.sleep(30)
    browser.quit()
