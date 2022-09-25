import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select



def calc(a,b):
    return str(int(a.text) + int(b.text))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    num3 = calc(num1,num2)
    select = Select(browser.find_element(By.CSS_SELECTOR, 'select'))
    select.select_by_value(num3)
    option1 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    option1.click()

finally:
    time.sleep(6)
    browser.quit()

