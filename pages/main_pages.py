from .base_pages import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """класс - наследник BasePage"""

    # заглушка, т.к. методы перенесены в base_pages
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
