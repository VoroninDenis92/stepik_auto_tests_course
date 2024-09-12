from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
   
    form_input = browser.find_element(By.ID, "answer")
    form_input.send_keys(y)

    chk_i_robot = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    chk_i_robot.click()

    robot_rules = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robot_rules.click()

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()