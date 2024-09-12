from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import unittest

class TestAbs(unittest.TestCase):
    def test_required1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        name_field = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.first_class .form-control.first')
        name_field.send_keys("Ivan")

        surname_field = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.second_class .form-control.second')
        surname_field.send_keys("Petrov")

        email_field = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.third_class .form-control.third')
        email_field.send_keys("e@mail.com")

        phone_field = browser.find_element(By.CSS_SELECTOR, '.second_block .form-group.first_class .form-control.first')
        phone_field.send_keys("2-44-32")

        address_field = browser.find_element(By.CSS_SELECTOR, '.second_block .form-group.second_class .form-control.second')
        address_field.send_keys("Default City")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")
        
    def test_required2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        name_field = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.first_class .form-control.first')
        name_field.send_keys("Ivan")

        surname_field = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.second_class .form-control.second')
        surname_field.send_keys("Petrov")

        email_field = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.third_class .form-control.third')
        email_field.send_keys("e@mail.com")

        phone_field = browser.find_element(By.CSS_SELECTOR, '.second_block .form-group.first_class .form-control.first')
        phone_field.send_keys("2-44-32")

        address_field = browser.find_element(By.CSS_SELECTOR, '.second_block .form-group.second_class .form-control.second')
        address_field.send_keys("Default City")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()