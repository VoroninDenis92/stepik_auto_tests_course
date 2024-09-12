from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()

    browser.switch_to.window(browser.window_handles[1])

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
   
    form_input = browser.find_element(By.ID, "answer")
    form_input.send_keys(y)

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()


finally:
    time.sleep(30)
    browser.quit()