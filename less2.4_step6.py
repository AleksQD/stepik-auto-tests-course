from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.get(link)
    

    browser.find_element_by_id("button")

    

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
