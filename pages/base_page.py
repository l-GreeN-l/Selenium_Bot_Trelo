# ----------------------------------------------------------------------------------------------------------------------
#
#                   Шаблон страницы
#
# ----------------------------------------------------------------------------------------------------------------------

from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, 5)

    def open(self):
        print('\n--> Opening browser......')
        self.browser.get(self.url)

    # Изменено возвращаемое значение
    def is_element_present(self, method, selector):
        try:
            self.to_wait(wait=WebDriverWait(self.browser, 5), locator=(method, selector))
            obj = self.browser.find_element(method, selector)
        except (NoSuchElementException):
            print('> Element not search: ', selector[1])
            return False
        return obj

    # Вернуть на предыдущую страницу
    def go_back(self):
        self.browser.back()

    # Обновить страницу
    def refresh(self):
        self.browser.refresh()

    # Сделать скриншот
    def screenshot(self, file_name='screenshot.png'):
        self.browser.save_screenshot(file_name)

    # Получить текущий url
    def get_current_url(self):
        return self.browser.current_url

    def to_wait(self, wait, locator, messange=""):
        try:
            wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException as ex:
            print(messange, '\n', ex)
