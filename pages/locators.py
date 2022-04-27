from selenium.webdriver.common.by import By

class ManePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_COAST = (By.CSS_SELECTOR, ".product_main > .price_color")
    ITEM_IN_CART_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    ITEM_IN_CART_NAME = (By.CSS_SELECTOR, "#messages strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

#Проверочный тег - "#product_description h2"