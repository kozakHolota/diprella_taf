import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as fOptions

from conf.web_drivers import WebDriver


class check_web_driver(object):
    web_driver: webdriver.remote = None

    @classmethod
    def close(cls):
        cls.web_driver.quit()

    def __init__(self, uri):
        self.uri = uri

    def __call__(self, page_object):
        wd_class = WebDriver[os.environ['webdriver.class']]
        if not check_web_driver.web_driver:
            if wd_class == WebDriver.FIREFOX:
                _browser_profile = webdriver.FirefoxProfile()
                _browser_profile.set_preference("dom.webnotifications.enabled", False)
                options = fOptions()
                #options.set_headless(headless=True)
                check_web_driver.web_driver = webdriver.Firefox(executable_path=os.environ['webdriver.path_to_driver'],
                                                      firefox_options=options,
                                                      options=_browser_profile)
            elif wd_class == WebDriver.CHROME:
                chrome_options = Options()
                #chrome_options.add_argument("--headless")
                prefs = {"profile.default_content_setting_values.notifications": 2}
                chrome_options.add_experimental_option("prefs", prefs)
                check_web_driver.web_driver = webdriver.Chrome(executable_path=os.environ['webdriver.path_to_driver'],
                                                     options=chrome_options)
            elif wd_class == WebDriver.IE:
                check_web_driver.web_driver = webdriver.Ie(executable_path=os.environ['webdriver.path_to_driver'])

            url = os.environ['webdriver.portal_url']
            full_url = f"{url}/{self.uri}" if "https://" in url else f"https://{url}/{self.uri}"
            check_web_driver.web_driver.maximize_window()
            check_web_driver.web_driver.get(full_url)

        return page_object