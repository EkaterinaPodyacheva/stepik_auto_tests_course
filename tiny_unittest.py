import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class test_class_name(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        input1.send_keys('QWERty')
        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        input1.send_keys('Qwerrty')
        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        input1.send_keys('katrin@gmail.com')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "все правильно")

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        input1.send_keys('QWERty')
        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        input1.send_keys('Qwerrty')
        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        input1.send_keys('katrin@gmail.com')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "нет элемента ввода Фамилии")


if __name__ == "__main__":
    unittest.main()
