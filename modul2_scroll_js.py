import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")         # скролим стр
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check.click()
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    button.click()
finally:
    time.sleep(15)
    browser.quit()
