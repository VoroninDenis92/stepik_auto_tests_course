from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value").text
    y = calc(x_element)
    
    form_input = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", form_input)
    form_input.send_keys(y)

    chk_i_robot = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", chk_i_robot)
    chk_i_robot.click()

    robot_rules = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rules)
    robot_rules.click()

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()