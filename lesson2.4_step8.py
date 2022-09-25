import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')
def calc(a):
    return str(math.log(abs(12*math.sin(int(a.text)))))

try:
    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )
    book = browser.find_element(By.ID, 'book')
    book.click()
    x = browser.find_element(By.ID, 'input_value')
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(x))
    option3 = browser.find_element(By.ID, 'solve')
    option3.click()

finally:
    time.sleep(7)
    browser.quit()