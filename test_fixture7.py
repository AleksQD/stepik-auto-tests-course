from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
import time
import math


less_list = ['https://stepik.org/lesson/236895/step/1',
             'https://stepik.org/lesson/236896/step/1',
             'https://stepik.org/lesson/236897/step/1',
             'https://stepik.org/lesson/236898/step/1',
             'https://stepik.org/lesson/236899/step/1',
             'https://stepik.org/lesson/236903/step/1',
             'https://stepik.org/lesson/236904/step/1',
             'https://stepik.org/lesson/236905/step/1'
             ]




@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', less_list)
def test_guest_should_see_login_link(browser, links):
    link = links
    text_in = ''
    browser.get(link)

    text_area = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ember-text-area"))
    )
    answer = math.log(int(time.time()))
    text_area.send_keys(str(answer))

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()

    message = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    #message = browser.find_element_by_class_name("smart-hints__hint")
    text = message.text
    if "Correct!" != text:
        text_in += text
        print(text_in)

    assert "Correct!" == text,  f"Wrong text, text = '{text}' "



