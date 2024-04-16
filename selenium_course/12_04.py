from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    elements = browser.find_elements(By.TAG_NAME,'input')
    for i in elements:
        if i=='[class="form-control first"]' or '[class="form-control second"]' or '[class="form-control third"]':
        i.send_keys('hi')
    button = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    time.sleep(5)
    button.click()
finally:
    time.sleep(30)
    browser.quit()