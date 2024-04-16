from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")
    button_1 = browser.find_element(By.NAME,'firstname')
    button_1.send_keys('Dima')
    button_2= browser.find_element(By.NAME,'lastname')
    button_2.send_keys('A')
    button_3 = browser.find_element(By.NAME,'email')
    button_3.send_keys('Dima@mail.ru')

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(cur_dir, 'file1504.txt')
    element = browser.find_element(By.CSS_SELECTOR,'[type="file"]')
    element.send_keys(file_path)

   
    button = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    button.click()
    time.sleep(3)
finally:
    time.sleep(5)
    browser.quit()