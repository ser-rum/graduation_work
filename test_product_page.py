from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

def test_guest_can_add_product_to_basket(browser):
   link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
   page = ProductPage(browser, link)
   page.open()
   name = page.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
   print(name)
   coast = page.browser.find_element(*ProductPageLocators.PRODUCT_COAST).text
   print(coast)
   page.add_to_the_cart()
   page.should_be_right_name(name)
   page.should_be_right_coast(coast)