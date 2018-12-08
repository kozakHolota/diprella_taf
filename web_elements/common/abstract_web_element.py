import os
import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from conf.web_driver_decorators import check_web_driver


class AbstractWebElement(object):
    """Base class for all web elements"""

    def __init__(self, web_element: WebElement):
        self.__element = web_element

    @property
    def web_element(self):
        return self.__element

    @property
    def tag_name(self):
        return self.web_element.tag_name

    @property
    def text(self):
        return self.web_element.text

    def is_displayed(self):
        return self.__element.is_displayed()

    def is_enabled(self):
        return self.__element.is_enabled()

    def is_selected(self):
        return self.__element.is_selected()

    def get_attribute(self, attr):
        return self.__element.get_attribute(attr)

    def focus_web_element(self):
        ActionChains(check_web_driver.web_driver)\
            .move_to_element(self.__element)\
            .click(self.__element).perform()

    def focus_web_element_js(self):
        check_web_driver.web_driver.execute_script("arguments[0].focus();", self.__element)

    def pull_web_element_to_background_js(self):
        check_web_driver.web_driver.execute_script\
            (
                "arguments[0].style.display = 'none';",
                self.__element
            )

    def focus_and_fill_field(self, text: str):
        ActionChains(check_web_driver.web_driver)\
            .move_to_element(self.__element)\
            .click()\
            .send_keys_to_element(self.__element, text)\
            .perform()

    def take_screenshot(self):
        self.__element.screenshot(
            os.path.join(
                os.path.curdir,
                'test_data',
                'screenshots',
                f'web_element_screenshot_{datetime.datetime.utcnow()}.png'
            )
        )