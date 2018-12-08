from enum import Enum
from functools import wraps

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conf.web_driver_decorators import check_web_driver
from utils.logging import Logging
from web_elements.common.abstract_web_element import AbstractWebElement


class FindStrategies(Enum):
    XPATH = (By.XPATH)
    CSS_SELECTOR = (By.CSS_SELECTOR)
    ID = (By.ID)
    CLASS_NAME = (By.CLASS_NAME)
    LINK_TEXT = (By.LINK_TEXT)
    PARTIAL_LINK_TEXT = (By.PARTIAL_LINK_TEXT)
    NAME = (By.NAME)

    def __init__(self, by: By):
        self.meth = by

    def find_element(self, expression: str, expected_condition=EC.presence_of_element_located, timeout=30):
        return WebDriverWait(check_web_driver.web_driver, timeout).until(
                    expected_condition((self.meth, expression))
        )

    def __str__(self):
        return self.name


class find_by(object):
    def __init__(self, find_strategy: FindStrategies, expression: str, web_element_class: AbstractWebElement, expected_condition=EC.presence_of_element_located, timeout=30):
        self.timeout = timeout
        self.expected_condition = expected_condition
        self.find_strategy = find_strategy
        self.expression = expression
        self.web_element_class = web_element_class

    def __call__(self, f):
        @wraps(f)
        def wrapper(_self):
            Logging.logger.info("Searching for WebElement with method {} and expression: {}".format(self.find_strategy, self.expression))
            return self.find_strategy.find_element(self.expression, self.expected_condition, self.timeout)

        return wrapper