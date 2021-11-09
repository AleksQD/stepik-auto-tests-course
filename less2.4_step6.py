from selenium import webdriver
import time


try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.get(link)

    browser.find_element_by_id("button")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
