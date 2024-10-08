from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    sum = str(int(browser.find_element(By.ID, "num1").text) +  int(browser.find_element(By.ID, "num2").text))
    print(sum)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(sum)

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()