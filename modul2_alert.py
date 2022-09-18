import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    input1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    alert = browser.switch_to.alert    #принимаем alert
    alert.accept()
    #решаем пример
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y) #вводим ответ

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    #копируем код ответа в терминал
    alert_answer = browser.switch_to.alert.text    #принимает alert-текст
    answer = alert_answer.split(':')[-1]
    print(answer)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(0.5)
    # закрываем браузер после всех манипуляций
    browser.quit()
