from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/get_attribute.html")
    element = browser.find_element(By.TAG_NAME, 'img')
    x = element.get_attribute('valuex')
    a=math.log(abs(12*math.sin(int(x))))
    print(x)
    time.sleep(3)
    resheniye=browser.find_element(By.ID,'answer')
    resheniye.send_keys(a)
    button_1 = browser.find_element(By.ID,'robotCheckbox')
    button_1.click()
    button_2= browser.find_element(By.ID,'robotsRule')
    button_2.click()
    button_3 = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    button_3.click()
    time.sleep(10)
finally:
    time.sleep(10)
    browser.quit() 