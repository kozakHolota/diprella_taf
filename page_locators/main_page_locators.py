from page_locators.abstract_locator_enum import AbstractLocatorEnum
from web_elements.common.div import Div
from web_elements.common.h import H
from web_elements.common.link import Link
from web_elements.common.p import P
from web_elements.common.text_field import TextField
from web_elements.finders.find_by import FindStrategies


class MainPageLocators(AbstractLocatorEnum):
    SIGNUP_BUTTON = (FindStrategies.CSS_SELECTOR, "app-header a[href$=sign-up]", Link)
    DIPRELLA_LOGO = (FindStrategies.CLASS_NAME, "logo__link", Link)
    SEARCH_FIELD = (FindStrategies.ID, "search", TextField)
    LOGIN_LINK = (FindStrategies.CSS_SELECTOR, ".header__nav [routerlink$=sign-in]", Link)
    LIBRARY_LINK = (FindStrategies.CSS_SELECTOR, "p.library__text", P)
    DESCRIPTION_HEADER = (FindStrategies.CSS_SELECTOR, "h1.banner__title", H)
    DESCRIPTION_TEXT = (FindStrategies.CSS_SELECTOR, "div.banner__text", Div)