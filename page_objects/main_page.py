from conf.web_driver_decorators import check_web_driver
from page_locators.main_page_locators import MainPageLocators
from page_objects.abstract_page import AbstractPage
from web_elements.finders.find_by import find_by


@check_web_driver(uri="")
class MainPage(AbstractPage):
    @property
    @find_by(*MainPageLocators.SIGNUP_BUTTON)
    def signup_button(self):
        pass

    @property
    @find_by(*MainPageLocators.DIPRELLA_LOGO)
    def diprella_logo(self):
        pass

    @property
    @find_by(*MainPageLocators.SEARCH_FIELD)
    def search_field(self):
        pass

    @property
    @find_by(*MainPageLocators.LOGIN_LINK)
    def login_link(self):
        pass

    @property
    @find_by(*MainPageLocators.LIBRARY_LINK)
    def library_link(self):
        pass

    @property
    @find_by(*MainPageLocators.DESCRIPTION_HEADER)
    def description_header(self):
        pass

    @property
    @find_by(*MainPageLocators.DESCRIPTION_TEXT)
    def description_text(self):
        pass