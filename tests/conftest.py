import time
import pytest
from selenium import webdriver
# from config import http_proxy
from selenium.webdriver.chrome.options import Options
import os
import datetime


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """
        Extends the PyTest Plugin to take and embed screenshots in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Директория скринов отчета
            report_directory = f'{os.getcwd()}/reports'
            now = str(int(round(time.time() * 1000)))
            # Строка дает ПАПКУ с модулем а также его классом и методом , где произошла ошибка
            path = report.nodeid.replace("::", "_")
            print(path)
            # path = path.split('/')[1] # Искключаем 'front_tests/' из пути
            file_name = path + f"_{now}.png"
            print(file_name)
            full_path = os.path.join(report_directory, file_name)

            if item.funcargs.get('browser'):
                print(f"[INFO] screenshot: {full_path}")
                item.funcargs['browser'].get_screenshot_as_file(full_path)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:600px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
        report.extra = extra


# Фикстура для открытия браузера и его закрытия после завершения тестирования
@pytest.fixture(scope="function", autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    prefs = {"download.default_directory": "/Selenium_Bot_Trelo/downloads"}
    chrome_options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default=None, help="Choose url for test")
    parser.addoption('--login', action='store', default="admin", help="Choose login")
    parser.addoption('--password', action='store', default="admin", help="Choose password")
    parser.addoption('--boardname', action='store', default="Kanban test", help="Choose board")
    parser.addoption('--groupname', action='store', default="Backlog", help="Choose group")
    parser.addoption('--member', action='store', default="admin", help="Choose member")
    parser.addoption('--labels', action='store', default=None, help="Choose filename.txt with labels")
    parser.addoption('--location', action='store', default="Russia", help="Choose location")
    parser.addoption('--cardname', action='store', default="AutoTest", help="Choose cardname")


@pytest.fixture(scope="session", autouse=True)
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session", autouse=True)
def login(request):
    return request.config.getoption("--login")


@pytest.fixture(scope="session", autouse=True)
def password(request):
    return request.config.getoption("--password")


@pytest.fixture(scope="session", autouse=True)
def boardname(request):
    return request.config.getoption("--boardname")


@pytest.fixture(scope="session", autouse=True)
def groupname(request):
    return request.config.getoption("--groupname")


@pytest.fixture(scope="session", autouse=True)
def member(request):
    return request.config.getoption("--member")


@pytest.fixture(scope="session", autouse=True)
def labels(request):
    return request.config.getoption("--labels")


@pytest.fixture(scope="session", autouse=True)
def location(request):
    return request.config.getoption("--location")


@pytest.fixture(scope="session", autouse=True)
def cardname(request):
    return request.config.getoption("--cardname")
