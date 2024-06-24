from .base_pages import BasePage
from .main_pages import MainPage
from .login_page import LoginPage
from .product_page import ProductPage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .locators import BasketPageLocators
from .basket_page import BasketPage


__all__ = [
    "BasePage",
    "LoginPage",
    "MainPage",
    "MainPageLocators",
    "LoginPageLocators",
    "ProductPage",
    "BasketPageLocators",
    "BasketPage",
]
