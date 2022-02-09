# ......................................................................................................................
#
#           Страница рабочего пространства с бордами в трелло
#
# ......................................................................................................................

import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class WorkspacePageLocators():
    WORKSPACE_PAGE  = (By.XPATH, '//*[@id ="trello-root"]')


class SideBarPanelLocators():
    TAB_BOARDS = (By.XPATH, '//*[contains(@data-test-id ,"home-team-boards-tab")]')


class TabBoardLocators():
    WORKSPACE_BOARDS = (By.XPATH, '//*[contains(@class, "boards-page-board-section-list")]')
    BOARD = (By.XPATH, '//*[contains(@class, "boards-page-board-section-list-item")]')
    CREATE_NEW_BOARD = (By.XPATH, '//*[contains(@data-test-id ,"create-board-tile")]')


class WorkspacePage(BasePage):

    # Перейти во вкладку Boards
    def go_to_tab_boards(self):
        self.is_element_present(*SideBarPanelLocators.TAB_BOARDS).click()

    # Найти доску
    def find_board(self, boardname):
        boards = self.browser.find_elements(*TabBoardLocators.BOARD)
        for board in boards:
            try:
                title = (By.XPATH, f'.//*[contains(@title, "{boardname}")]')
                if board.find_element(*title):
                    return board
            except NoSuchElementException as ex:
                print('Доска не найдена \n', ex)

    # Перейти в определенную доску
    def go_to_board(self, boardname):
        self.find_board(boardname).click()
