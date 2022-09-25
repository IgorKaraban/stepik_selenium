from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)
def calc(a):
    return str(math.log(abs(12*math.sin(int(a.text)))))

try:
    btn = browser.find_element(By.CSS_SELECTOR, '.trollface.btn')
    btn.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.CSS_SELECTOR, '#input_value')
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(calc(x))
    option3 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    option3.click()



finally:
    time.sleep(6)
    browser.quit()