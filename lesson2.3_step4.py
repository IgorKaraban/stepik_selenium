import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)
def calc(a):
    return str(math.log(abs(12*math.sin(int(a.text)))))

try:
    btn = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    btn.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value')
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(calc(x))
    option3 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    option3.click()



finally:
    time.sleep(5)
    browser.quit()