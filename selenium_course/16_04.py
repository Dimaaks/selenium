from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    button.click()
 
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID,'input_value')

    el1 = x.text
    e1=int(el1)

    a=math.log(abs(12*math.sin(e1)))
    element_text=str(a)

    element1 = browser.find_element(By.ID,'answer')
    element1.send_keys(element_text)
    time.sleep(2)
    button1 = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    button1.click()

    
finally:
    time.sleep(5)
    browser.quit()