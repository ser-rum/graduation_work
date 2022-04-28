from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_the_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_be_right_name(self, name):
        assert name == self.browser.find_element(*ProductPageLocators.ITEM_IN_CART_NAME).text, \
            "The name doesn`t match"

    def should_be_right_coast(self, coast):
        assert coast == self.browser.find_element(*ProductPageLocators.ITEM_IN_CART_PRICE).text, \
            "The coast in the cart doesn`t match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_is_disappear(self):
        self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should"
