# ......................................................................................................................
#
#           Страница входа в трелло
#
# ......................................................................................................................



import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPageLocators():
    BTN_INPUT  = (By.XPATH, '//*[contains(@href, "/login")]')
    LOGIN = (By.XPATH, '//input[contains(@name, "user") ][contains(@class,"form-field")]')
    PASSWORD = (By.XPATH, '//input[contains(@name, "password") ][contains(@class,"form-field")]')
    LOGIN_BUTTON = (By.XPATH, '//*[contains(@id, "login") ][contains(@value,"Войти")]')

    # Вход с акк атлассиан
    ATL_PASS = (By.XPATH, '//input[@name="password"]')
    ATL_INP = (By.XPATH, '//*[@id="login-submit"]')

class LoginPage(BasePage):

    def login(self, login, password):
        pageloc = LoginPageLocators()
        self.is_element_present(*pageloc.BTN_INPUT).click()
        time.sleep(2)
        self.is_element_present(*pageloc.LOGIN).send_keys(login)
        time.sleep(2)
        self.is_element_present(*pageloc.LOGIN_BUTTON).click()
        # Переход на страницу атлассиан
        time.sleep(2)
        self.is_element_present(*pageloc.ATL_PASS).send_keys(password)
        self.is_element_present(*pageloc.ATL_INP).click()

