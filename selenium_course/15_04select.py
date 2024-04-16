from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects2.html")
    element1 = browser.find_element(By.ID,'num1')
    el1 = element1.text
    e1=int(el1)
    element2 = browser.find_element(By.ID,'num2')
    el2 = element2.text
    e2=int(el2)
    element=e1+e2
    element_text=str(element)
    select = Select(browser.find_element(By.TAG_NAME,'select'))
    select.select_by_value(element_text)
    button = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    button.click()
    time.sleep(3)
finally:
    time.sleep(5)
    browser.quit()