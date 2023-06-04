# ......................................................................................................................
#
#           Страница Доски(Board)
#
# ......................................................................................................................

import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import random


class BoardPageLocators():
    BOARDS_PAGE_PANEL = (By.XPATH, '//*[contains(@class,"board-main-content")]')  # Основной контент страницы с доской
    GROUP = (By.XPATH, '//*[@id="board"]/*[contains(@class,"js-list list-wrapper")]')  # Группы (колонки)
    GROUP_NAME = (By.XPATH, '//textarea[contains(@class,"list-header-name")]')  # Имя группы
    CARD = (By.XPATH, '//*[contains(@class,"list-card")][contains(@href,"/")]')  # Карточка
    CARD_NAME = (By.XPATH, './/*[contains(@class,"list-card-title")]')  # имя карточки
    BTN_ADD_CARD = (By.XPATH, './/*[contains(@class,"open-card-composer")]')  # Добавить новую карточку
    TF_NEW_CARD = (By.XPATH, './/*[contains(@class,"list-card-composer-textarea")]')  # Название новой карточки
    CLOSE_NEW_CARD = (By.XPATH, '//*[contains(@class,"cc-controls-section")]/*[contains(@class,"icon-close")]')


class BoardPage(BasePage):
    pageloc = BoardPageLocators()

    # Найти группу
    def find_group(self, groupname):
        groups = self.browser.find_elements(*self.pageloc.GROUP)
        for group in groups:
            name = group.find_element(*self.pageloc.GROUP_NAME).text
            if name == groupname:
                return group
        return False

    # Ищет карточку в группе или по всей доске
    def find_card(self, group=None, cardname=False):
        # Если группа задана - ищем в группе
        if group:
            cards_of_group = group.find_elements(*self.pageloc.CARD)
            for card in cards_of_group:
                name = card.find_element(*self.pageloc.CARD_NAME).text
                if name == cardname:
                    return card
            return False
        # Если группа не задана - ищем по всей доске
        else:
            all_cards = self.browser.find_elements(*self.pageloc.CARD)
            for card in all_cards:
                name = card.find_element(*self.pageloc.CARD_NAME).text
                if name == cardname:
                    return card
            return False

    # Перейти в карточку
    def go_to_card(self, cardname):
        time.sleep(0.5)
        card = self.find_card(cardname=cardname)
        if card:
            card.click()
        else:
            raise NoSuchElementException('Карточка не найденна')

    # Создать новую карточку
    def create_new_card(self, groupname, cardname=None):
        group = self.find_group(groupname)
        group.find_element(*self.pageloc.BTN_ADD_CARD).click()
        self.to_wait(self.wait, self.pageloc.TF_NEW_CARD)
        text_field = group.find_element(*self.pageloc.TF_NEW_CARD)
        if cardname:
            text_field.send_keys(cardname)
        else:
            cardname = 'AutoTest' + str(random.randint(100))
            text_field.send_keys(cardname)
        text_field.send_keys(Keys.ENTER)
        self.is_element_present(*self.pageloc.CLOSE_NEW_CARD).click()
