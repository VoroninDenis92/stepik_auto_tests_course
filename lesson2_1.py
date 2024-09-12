from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "treasure").get_attribute('valuex')
    x = x_element
    y = calc(x)
   
    form_input = browser.find_element(By.ID, "answer")
    form_input.send_keys(y)

    chk_i_robot = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    chk_i_robot.click()

    robot_rules = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    robot_rules.click()

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()