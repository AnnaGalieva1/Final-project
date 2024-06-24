import pages
import pytest


pages.ProductPage
pages.BasePage
pages.BasketPage
pages.LoginPage
pages.LoginPageLocators


@pytest.mark.parametrize(
    "link",
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail(reason="bug"),
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
    ],
)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = pages.ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.should_be_message_product_added_to_basket()
    page.correct_product_name_in_message()
    page.should_be_message_basket_price()
    page.correct_basket_price()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = pages.BasePage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = pages.BasePage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = pages.BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_no_items_in_basket()
    page.should_be_message_basket_is_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        from random_word import RandomWords

        r = RandomWords()
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = pages.LoginPage(browser, link)
        email = self.email = r.get_random_word() + "@mail.com"
        password = self.password = r.get_random_word() + "123"
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = pages.ProductPage(browser, link)
        page.open()
        page.should_be_not_success_message_is_not_element_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

        page = pages.ProductPage(browser, link)
        page.open()
        page.add_to_cart_button()
        page.solve_quiz_and_get_code()
        page.should_be_message_product_added_to_basket()
        page.correct_product_name_in_message()
        page.should_be_message_basket_price()
        page.correct_basket_price()
