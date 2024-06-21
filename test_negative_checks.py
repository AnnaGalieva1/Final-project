import pages

pages.ProductPage


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = pages.ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.should_be_not_success_message_is_not_element_present()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = pages.ProductPage(browser, link)
    page.open()
    page.should_be_not_success_message_is_not_element_present()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = pages.ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.should_be_not_success_message_is_element_disappeared()
