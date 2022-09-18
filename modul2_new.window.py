import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/redirect_accept.html")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    new_window = driver.window_handles[1]
    driver.switch_to.window(driver.window_handles[1])
    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    answer = driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y) #вводим ответ

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    #копируем код ответа в терминал
    alert_answer = driver.switch_to.alert.text    #принимает alert-текст
    answer = alert_answer.split(':')[-1]
    print(answer)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(0.5)
    # закрываем браузер после всех манипуляций
    driver.quit()
