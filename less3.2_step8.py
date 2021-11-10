from selenium import webdriver
import time
import unittest


class TestRegist(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.assertEqual("Congratulations! You have successfully registered!",
                         sel_script(link))

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.assertEqual("Congratulations! You have successfully registered!", -
                         sel_script(link))


def sel_script(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector(
        '.first[required = ""]')
    first_name.send_keys("test")

    last_name = browser.find_element_by_css_selector(
        '.second[required = ""]')
    last_name.send_keys("test")

    mail = browser.find_element_by_css_selector(
        '.third[required = ""]')
    mail.send_keys("test")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # закрываем браузер после всех манипуляций
    browser.quit()
    return welcome_text


if __name__ == "__main__":
    unittest.main()
