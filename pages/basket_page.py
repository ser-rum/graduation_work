from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), \
            "Basket is not empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "\"Empty Basket\" message is not presented"
