import unittest
import pytest
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


alien_text = ''
links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1'
         ]


@pytest.mark.parametrize('links', links)
def test_aliens_text(browser, links):
    global alien_text
    browser.get(links)
    answer = math.log(int(time.time()))

    text_area = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ember-text-area"))
    )
    text_area.send_keys(str(answer))

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()

    message = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "smart-hints__hint"))
    )

    text = message.text

    try:
        assert "Correct!" == text
    except AssertionError:
        alien_text += text
        print(alien_text)
