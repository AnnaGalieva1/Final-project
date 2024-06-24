from .locators import BasketPageLocators
from .base_pages import BasePage


class BasketPage(BasePage):
    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM), "Item in basket"

    def should_be_message_basket_is_empty(self):
        assert self.browser.find_element(
            *BasketPageLocators.BASKET_EMPTY
        ), "Message that basket is empty not found"
