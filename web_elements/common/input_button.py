from selenium.webdriver.remote.webelement import WebElement

from web_elements.common.abstract_web_element import AbstractWebElement
from web_elements.common_operations.click_operations import click, focus_and_click, click_js

@click
@focus_and_click
@click_js
class InputButton(AbstractWebElement):

    def __init__(self, web_element: WebElement):
        super().__init__(web_element)

    @property
    def text(self):
        return self.web_element.get_attribute("value")