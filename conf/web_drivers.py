from enum import Enum, auto


class WebDriver(Enum):
    FIREFOX = auto()
    CHROME = auto()
    IE = auto()

    def __str__(self):
        return  self.name