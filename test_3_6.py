import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
def test_answer_aliens(browser, links):
    link = f"{links}/"
    browser.get(link)
    browser.implicitly_wait(10)
    textarea = browser.find_element(By.CSS_SELECTOR, ".textarea")
    textarea.send_keys(str(math.log(int(time.time()))))
    print(str(math.log(int(time.time()))))
    browser.implicitly_wait(10)

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']")))
    button.click()

    element_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text

    assert element_text == "Correct!"