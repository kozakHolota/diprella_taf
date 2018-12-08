from selenium.webdriver import ActionChains

from conf.web_driver_decorators import check_web_driver


def fill_field(web_elem_to_fill=None):
    def wrapped(web_elem):
        def fill_field(self, text: str):
            if web_elem_to_fill:
                web_elem_to_fill.send_keys(text)
            else:
                self.web_element.send_keys(text)

        web_elem.fill_field = fill_field

        return web_elem

    return wrapped


def fill_field_js(web_elem_to_fill=None):
    def wrapped(web_elem):
        def tmp_action(elem, text):
            check_web_driver.web_driver.execute_script \
                 (
                 f"arguments[0].value = '{text}';",
                 elem
             )

        def fill_field_js(self, text: str):
            if web_elem_to_fill:
                tmp_action(web_elem_to_fill, text)
            else:
                tmp_action(self.web_element, text)

        web_elem.fill_field_js = fill_field_js

    return wrapped


def focus_and_fill_field(web_elem_to_fill=None):
    def wrapped(web_elem):
        def tmp_action(elem, text):
            ActionChains(check_web_driver.web_driver) \
             .move_to_element(elem) \
             .click() \
             .send_keys_to_element(elem, text) \
             .perform()

        def focus_and_fill_field(self, text: str):
            if web_elem_to_fill:
                tmp_action(web_elem_to_fill, text)
            else:
                tmp_action(self.web_element, text)

        web_elem.focus_and_fill_field = focus_and_fill_field

    return wrapped