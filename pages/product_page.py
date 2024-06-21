from .base_pages import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart_button(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON)
        button.click()

    # Проверка сообщения об успешном добавлении товара в корзину
    def should_be_message_product_added_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ADDED_TO_BASKET
        ), "There is no message to add"

    # Проверка названия товара в сообщении о добавлении в корзину
    def correct_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(
            *ProductPageLocators.ADDED_TO_BASKET
        ).text
        assert product_name == message_name, "The product name not found on message"

    # Проверка сообщения о стоимости корзины
    def should_be_message_basket_price(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_PRICE
        ), "There is no message to basket price"

    # Проверка стоимости товара и стоимости корзины
    def correct_basket_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        assert (
            product_price == basket_price
        ), "the product price differs from the basket price"

    def should_be_not_success_message_is_not_element_present(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ADDED_TO_BASKET
        ), "Success message is presented, but should not be"

    def should_be_not_success_message_is_element_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.ADDED_TO_BASKET
        ), "Success message is presented, but should not be"
