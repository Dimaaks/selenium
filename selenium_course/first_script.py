from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link) 
    input_1 = browser.find_element(By.NAME, 'first_name')
    input_1.send_keys('Timo')
    input_2 = browser.find_element(By.NAME, 'last_name')
    input_2.send_keys('Johansson')
    input_3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input_3.send_keys('Pietari')
    input_4 = browser.find_element(By.ID, 'country')
    input_4.send_keys('Venaja')
    
finally:
    time.sleep(5)
    browser.quit()
