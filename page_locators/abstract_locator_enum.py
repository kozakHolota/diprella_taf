from enum import Enum

from web_elements.common.abstract_web_element import AbstractWebElement
from web_elements.finders.find_by import FindStrategies


class AbstractLocatorEnum(Enum):
    def __init__(self,
                 find_strategy: FindStrategies,
                 expression: str,
                 web_element_class: AbstractWebElement):
        self.__locator = (find_strategy, expression, web_element_class)

    def __iter__(self):
        return self.__locator.__iter__()