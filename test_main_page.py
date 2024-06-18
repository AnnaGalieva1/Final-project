# Первый вариант импорта:
# from pages.main_pages import MainPage
# from pages.login_page import LoginPage

# Второй вариант импорта с объявлением списка классов в __init__
import pages

pages.MainPage
pages.LoginPage
# можно прописать полностью from pages import BasePage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = pages.MainPage(
        browser, link
    )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()
    login_page = pages.LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
