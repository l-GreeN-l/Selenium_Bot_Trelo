# ......................................................................................................................
#
#           Страница входа в трелло
#
# ......................................................................................................................


import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPageLocators:
    BTN_INPUT = (By.XPATH, '//*[contains(@href, "/login")]')
    LOGIN = (By.XPATH, '//input[contains(@name, "user") ][contains(@class,"form-field")]')
    PASSWORD = (By.XPATH, '//input[contains(@name, "password") ][contains(@class,"form-field")]')
    # LOGIN_WITH_ATL = (By.XPATH, '//*[contains(@id, "login") ][contains(@value,"Войти с помощью")]')
    NEXT = (By.XPATH, '//*[@type="submit"][contains(@value,"Продолжить")]')
    # Вход с акк атлассиан
    ATL_PASS = (By.XPATH, '//input[@name="password"]')
    ATL_INP = (By.XPATH, '//*[@id="login-submit"]')


class LoginPage(BasePage):

    def login(self, login, password):
        pageloc = LoginPageLocators()
        self.is_element_present(*pageloc.BTN_INPUT).click()
        self.is_element_present(*pageloc.LOGIN).send_keys(login)
        self.is_element_present(*pageloc.NEXT).click()
        self.to_wait(self.wait, pageloc.ATL_PASS)

        # Переход на страницу атлассиан
        self.is_element_present(*pageloc.ATL_PASS).send_keys(password)
        self.is_element_present(*pageloc.ATL_INP).click()
