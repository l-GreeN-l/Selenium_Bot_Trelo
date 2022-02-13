# ......................................................................................................................
#
#           Меню карточки
#
# ......................................................................................................................


import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class CardPageLocators():

        TA_DESCRIPTION_BTN = (By.XPATH, '//*[contains(@class, "u-gutter")]/*[contains(@class,"editable")]')
        TA_DESCRIPTION_EDIT = (By.XPATH, '//*[contains(@class, "description-edit")]/textarea[contains(@class,"field")]')
        TA_DESCRIPTION_BTN_SAVE = (By.XPATH, '//*[contains(@class, "description-edit")]/descendant::*[contains(@value, "Save")]')
        TA_DESCRIPTION = (By.XPATH, '//*[contains(@class, "current markeddown")]/*')
        TA_COMMENT = (By.XPATH, '//*[contains(@class, "comment-box")]/*[contains(@class, "comment-box-input")][contains(@placeholder, "Write a comment")]')
        TA_COMMENT_SAVE = (By.XPATH, '//*[contains(@class, "comment-frame")]/descendant::*[contains(@value, "Save")]')
        BTN_CLOSE_CARD = (By.XPATH, '//*[contains(@class, "close-window")]')

        # Кнопки добавить и поля к ним
        # Закрыть любое из меню - универсальный локатор
        BTN_CLOSE_ALL_MENU = (By.XPATH, '//*[contains(@class, "pop-over-header-close")]')

        BTN_ADD_MEMBER = (By.XPATH, '//*[contains(@title, "Members")]')
        TF_MEMBER = (By.XPATH, '//*[contains(@placeholder, "Search members")]')
        MEMBER = (By.XPATH, '//*[@class="name js-select-member"]')

        BTN_ADD_LABEL = (By.XPATH, '//*[contains(@title, "Labels")]')
        TF_LABEL = (By.XPATH, '//*[contains(@placeholder, "Search labels")]')

        BTN_ADD_CHECKLIST = (By.XPATH, '//*[contains(@title, "Checklist")]')

        BTN_ADD_LOCATION = (By.XPATH, '//*[contains(@title, "Location")]')
        TF_LOCATION = (By.XPATH, '//*[contains(@placeholder, "Search Google Maps")]')
        TF_LOC_ITEM = (By.XPATH, '//*[contains(@class,"js-location-item")]')
        LOCATION = (By.XPATH, '//*[contains(@id,"js-static-map")]')

        BTN_MOVE = (By.XPATH, '//*[contains(@title, "Move")]')
        COMBO_LIST = (By.XPATH, '//*[contains(@class, "js-select-list")]')
        COMBO_LIST_ITEM_MENU = (By.XPATH, '//*[contains(@class, "js-select-list")]/option')
        BTN_MOVE_MOVE = (By.XPATH, '//*[contains(@value, "Move")]')

        # Шара
        BTN_SHARE = (By.XPATH, '//*[contains(@title, "Share")]')
        TF_SHARE_LINK = (By.XPATH, '//*[contains(@class, "js-short-url")]')
        BTN_DELL = (By.XPATH, '//*[contains(@class, "js-delete")][contains(text(), "Delete")]')
        YES_DELL = (By.XPATH, '//*[contains(@class, "js-confirm")]')

class CardPage(BasePage):

        pageloc = CardPageLocators()


        def add_member(self, name):
                self.is_element_present(*self.pageloc.BTN_ADD_MEMBER).click()
                self.is_element_present(*self.pageloc.TF_MEMBER).send_keys(name)
                self.is_element_present(*self.pageloc.MEMBER).click()
                self.is_element_present(*self.pageloc.BTN_CLOSE_ALL_MENU).click()

        def add_location(self, location):
                self.is_element_present(*self.pageloc.BTN_ADD_LOCATION).click()
                time.sleep(0.5)
                self.is_element_present(*self.pageloc.TF_LOCATION).send_keys(location)
                time.sleep(3)
                self.is_element_present(*self.pageloc.TF_LOCATION).send_keys(Keys.ENTER)
                self.to_wait(self.wait, self.pageloc.LOCATION)

        def add_label(self, labels):
                self.is_element_present(*self.pageloc.BTN_ADD_LABEL).click()
                for label in labels:
                        self.is_element_present(*self.pageloc.TF_LABEL).send_keys(label)
                        self.is_element_present(*self.pageloc.TF_LABEL).send_keys(Keys.ENTER)
                self.is_element_present(*self.pageloc.BTN_CLOSE_ALL_MENU).click()

        def dell_card(self, cardname):
                self.is_element_present(*self.pageloc.BTN_SHARE).click()
                self.is_element_present(*self.pageloc.BTN_DELL).click()
                self.is_element_present(*self.pageloc.YES_DELL).click()

        def move(self, groupname):
            pass