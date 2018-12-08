from selenium.webdriver.remote.webelement import WebElement

from web_elements.common.abstract_web_element import AbstractWebElement
from web_elements.common_operations.click_operations import click, focus_and_click, click_js
from web_elements.common_operations.fill_field_operations import fill_field, fill_field_js, focus_and_fill_field


@click
@focus_and_click
@click_js
@fill_field
@fill_field_js
@focus_and_fill_field
class TextField(AbstractWebElement):

    def __init__(self, web_element: WebElement):
        super().__init__(web_element)

    @property
    def text(self):
        return self.web_element.get_attribute("value")