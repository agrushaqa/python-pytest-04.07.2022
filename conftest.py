import pytest
from selenium import webdriver
from datetime import datetime
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def mail_credentials():
    return {
        "user": "xxx@yandex.ru",
        "password": "xxxx"
    }

@pytest.fixture(scope="session")
def draft_mail_content():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return {
        "to": "agrusha2021@gmail.com",
        "subject": "this is draft {}".format(dt_string),
        "body": "Artem Grusha"
    }

@pytest.fixture(scope="session")
def success_mail_content():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return {
        "to": "agrusha2021@gmail.com",
        "subject": "this is email for Artem Grusha {}".format(dt_string),
        "body": "this is autotest (c) agrusha"
    }

@pytest.fixture(scope="session")
def url():
    return 'http://mail.yandex.ru/'

@pytest.fixture(scope="session")
def browser(pytestconfig):
    print(f"my browser: {pytestconfig.getoption('browser')}")
    if pytestconfig.getoption('browser') == 'firefox' or pytestconfig.getoption('browser') == 'Firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="crome")