import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    elements = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    for element in elements:
        element.send_keys('done')
    file = browser.find_element(By.CSS_SELECTOR, "#file")
    file.send_keys(file_path)
    send = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    send.click()


finally:
    time.sleep(8)
    browser.quit()