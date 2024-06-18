from .base_pages import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    """класс - наследник BasePage"""

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK
        ), "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
