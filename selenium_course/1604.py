from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.ui import Select


import time
import math
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")



    btn = WebDriverWait(browser,100).until(es.text_to_be_present_in_element((By.ID,'price'),'100'))

    button = browser.find_element(By.ID,"book")
    button.click()

    x = browser.find_element(By.ID,'input_value')

    el1 = x.text
    e1=int(el1)

    a=math.log(abs(12*math.sin(e1)))
    element_text=str(a)

    element1 = browser.find_element(By.ID,'answer')
    element1.send_keys(element_text)
    button1 = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    button1.click()

    
finally:
    time.sleep(5)
    browser.quit()