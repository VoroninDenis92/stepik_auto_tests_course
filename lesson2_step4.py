from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_test = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    for item in input_test:
        item.send_keys('Ok')
    
    inp_file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson2_step4.txt') 
    inp_file.send_keys(file_path)

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "treasure").get_attribute('valuex')
    x = x_element
    y = calc(x)
   
    form_input = browser.find_element(By.ID, "answer")
    form_input.send_keys(y)

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()

finally:
    time.sleep(30)
    browser.quit()