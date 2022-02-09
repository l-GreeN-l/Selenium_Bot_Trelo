# ......................................................................................................................
#
#           Тест на добавлении карточки
#
#
# ......................................................................................................................


import time
from selenium.webdriver.common.keys import Keys
import datetime
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.trello.login_page import LoginPage, LoginPageLocators
from pages.trello.Workspace.workspace_page import WorkspacePage, WorkspacePageLocators, SideBarPanelLocators, TabBoardLocators
from pages.trello.Workspace.Board.board_page import BoardPage, BoardPageLocators
from pages.trello.Workspace.Board.Card.card_menu import CardPage, CardPageLocators


from tools import Instruments

class TestAddCard:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, login, password, url, boardname, groupname, member, labels, location, cardname):
        self.tools = Instruments()
        self.login = login
        self.password = password
        self.url = url
        self.boardname = boardname
        self.groupname = groupname
        self.member = member
        self.location = location
        self.cardname = cardname
        self.wait = WebDriverWait(browser, 5)
        print(self.cardname)
        if labels:
            file = open(labels,'r')
            list = []
            for str in file:
                str = str.split('\n')[0]
                list.append(str)
            self.labels = list
        self.page = LoginPage(browser, self.url)
        self.page.open()
        self.page.login(self.login, self.password)

    @pytest.mark.card
    @pytest.mark.smoke
    def test_add_card(self, browser):
        self.page.to_wait(self.wait,
                          WorkspacePageLocators.WORKSPACE_PAGE,
                          'Страница с рабочим пространством не открыватся')
        self.page.to_wait(self.wait,
                          SideBarPanelLocators.TAB_BOARDS,
                          'Не найденна вкладка boards')
        self.page = WorkspacePage(browser, self.url)
        self.page.go_to_tab_boards()
        self.page.to_wait(self.wait,
                          TabBoardLocators.WORKSPACE_BOARDS,
                          'Панель с бордами не открывается')
        self.page.to_wait(self.wait,
                          TabBoardLocators.BOARD,
                          'В панели с бордами не найденно ни одной доски')
        time.sleep(1)
        self.page.go_to_board(self.boardname)
        self.page = BoardPage(browser, self.url)
        self.page.to_wait(self.wait, BoardPageLocators.GROUP,)
        self.page.to_wait(self.wait, BoardPageLocators.BTN_ADD_CARD,)

        self.page.create_new_card(self.cardname,self.groupname)
        time.sleep(0.5)
        self.page.go_to_card(self.cardname)

        self.page = CardPage(browser, self.url)
        self.page.add_member(self.member)
        self.page.add_label(self.labels)
        self.page.add_location(self.location)

    @pytest.mark.card
    def test_dell_card(self, browser ):
        assert self.cardname, 'Карточка не создана'
        self.page = WorkspacePage(browser, self.url)
        self.page.go_to_tab_boards()
        self.page.to_wait(self.wait,
                          TabBoardLocators.BOARD,
                          'В панели с бордами не найденно ни одной доски')
        time.sleep(1)
        self.page.go_to_board(self.boardname)
        self.page = BoardPage(browser, self.url)
        self.page.to_wait(self.wait,
                          BoardPageLocators.GROUP,
                          'На доске нет ни одной группы')
        time.sleep(1)
        self.page.go_to_card(self.cardname)
        self.page = CardPage(browser, self.url)
        self.page.to_wait(self.wait,
                          CardPageLocators.TA_COMMENT,
                          'Карточка не загружена')
        self.page.dell_card(self.cardname)

