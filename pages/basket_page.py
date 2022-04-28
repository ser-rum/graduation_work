from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), \
            "Basket is not empty"

    '''def should_be_empty_basket_message(self):
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida",
            "cs": "Váš košík je prázdný",
            "da": "Din indkøbskurv er tom",
            "de": "Ihr Warenkorb ist leer",
            "en": "Your basket is empty",
            "el": "Το καλάθι σας είναι άδειο",
            "es": "Tu carrito esta vacío",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide",
            "it": "Il tuo carrello è vuoto",
            "ko": "장바구니가 비었습니다",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty",
            "pt": "O carrinho está vazio",
            "pt-br": "Sua cesta está vazia",
            "ro": "Cosul tau este gol",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий",
            "zh-cn": "Your basket is empty",
        }
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        print(message.split('. ')[0])
        assert languages[language] == message.split('.')[0], \
            "\"Empty Basket\" message is not presented"'''

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "\"Empty Basket\" message is not presented"