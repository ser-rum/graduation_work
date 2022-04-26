from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_the_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()
        self.solve_quiz_and_get_code()

    def should_be_right_name(self, name):
        assert name == self.browser.find_element(*ProductPageLocators.ITEM_IN_CART_NAME).text, "The name doesn`t match"

    def should_be_right_coast(self, coast):
        assert coast == self.browser.find_element(*ProductPageLocators.CART_PRICE).text, "The coast in the cart doesn`t match"