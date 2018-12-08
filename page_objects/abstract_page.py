import os
import datetime
from conf.web_driver_decorators import check_web_driver


class AbstractPage(object):
    def take_screenshot(self):
        check_web_driver.web_driver.get_screenshot_as_file(
            os.path.join(
                os.path.curdir,
                'test_data',
                'screenshots',
                f'screenshot_{datetime.datetime.utcnow()}.png'
            )
        )

