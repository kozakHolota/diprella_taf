import os

import pytest

from conf.web_driver_decorators import check_web_driver
from conf.web_drivers import WebDriver


def pytest_addoption(parser):
    parser.addoption("--firefox",
                     action='store_true',
                     default=False,
                     help="Start Firefox WebDriver")
    parser.addoption("--ie",
                     action='store_true',
                     default=False,
                     help="Start Internet Explorer WebDriver")
    parser.addoption("--google-chrome",
                     action='store_true',
                     default=False,
                     help="Start Google Chrome WebDriver")
    parser.addoption("--webdriver-location",
                     action='store',
                     help="Where to get the webdriver")
    parser.addoption("--portal_url",
                     action='store',
                     help="URL of the portal")
    # parser.addoption("--username",
    #                  action='store',
    #                  help="Username to login to")
    # parser.addoption("--password",
    #                  action='store',
    #                  help="Password to login to")

@pytest.fixture(scope='class', autouse=True)
def web_driver_setup(request):
    os.environ['webdriver.path_to_driver'] = pytest.config.getoption("--webdriver-location")
    os.environ['webdriver.portal_url'] = pytest.config.getoption("--portal_url")

    if pytest.config.getoption("--firefox"):
        os.environ['webdriver.class'] = str(WebDriver.FIREFOX)
    elif pytest.config.getoption("--ie"):
        os.environ['webdriver.class'] = str(WebDriver.IE)
    elif pytest.config.getoption("--google-chrome"):
        os.environ['webdriver.class'] = str(WebDriver.CHROME)
    else:
        raise ValueError("Incorrect browser")

@pytest.fixture(scope='function', autouse=True)
def load_app(request):
    from page_objects.main_page import MainPage
    request.cls.main_app = MainPage()
    def driver_close():
        check_web_driver.close()

    request.addfinalizer(driver_close)