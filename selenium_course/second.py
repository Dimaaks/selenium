from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "https://easysmarthub.ru/contact/"
try:
    browser = webdriver.Chrome()
    browser.get(link) 
    input_1 = browser.find_element(By.NAME, 'your-name')
    input_1.send_keys('Dima Aks')
    input_2 = browser.find_element(By.CLASS_NAME, 'wpcf7-form-control.wpcf7-text.wpcf7-email.wpcf7-validates-as-required.wpcf7-validates-as-email.form-control')
    input_2.send_keys('test@mail.ru')
    input_3 = browser.find_element(By.NAME, 'your-subject')
    input_3.send_keys('Testing')
    input_4 = browser.find_element(By.NAME, 'your-message')
    input_4.send_keys('Hello')
    button_ = browser.find_element(By.NAME, 'gdpr')
    button_.click()
    button_last = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_last.click()
finally:
    time.sleep(5)
    browser.quit()