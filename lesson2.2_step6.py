import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(a):
    return str(math.log(abs(12*math.sin(int(a.text)))))

try:
    x = browser.find_element(By.CSS_SELECTOR, '#input_value')
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    option1 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    browser.execute_script("window.scrollBy(0, 100);")
    input1.send_keys(calc(x))
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    option2.click()
    option3 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    option3.click()

finally:
    time.sleep(5)
    browser.quit()

