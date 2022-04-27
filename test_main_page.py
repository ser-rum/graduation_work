from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

"""def test_guest_can_go_to_login_page(browser):
   link = "http://selenium1py.pythonanywhere.com/"
   page = MainPage(browser, link)
   page.open()
   page.go_to_login_page()
   login_page = LoginPage(browser, browser.current_url)
   login_page.should_be_login_page()"""


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
   link = "http://selenium1py.pythonanywhere.com/"
   page = BasketPage(browser, link)
   page.open()
   page.go_to_basket_page()
   page.should_no_items_in_basket()
   page.should_be_empty_basket_message()

'''def test_guest_is_on_login_page(browser):
   link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
   page = LoginPage(browser, link)
   page.open()
   page.should_be_login_page()'''

#python -m pytest -s test_main_page.py