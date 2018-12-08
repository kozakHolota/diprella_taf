from selenium.webdriver.remote.webelement import WebElement

from web_elements.common.abstract_web_element import AbstractWebElement


class H(AbstractWebElement):

    def __init__(self, web_element: WebElement):
        super().__init__(web_element)