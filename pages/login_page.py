from .main_pages import MainPage
from .locators import LoginPageLocators


class LoginPage(MainPage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL does not contain a login"

    def should_be_login_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form not found"

    def should_be_register_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form not found"
