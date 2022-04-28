from selenium.webdriver.common.by import By

class ManePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FORM = (By.ID, "id_registration-email")
    PASSWORD_FORM = (By.ID, "id_registration-password1")
    PASSWORD_REPEAT_FORM = (By.ID, "id_registration-password2")
    AUTHORIZATION_BUTTON = (By.CSS_SELECTOR, "#register_form > .btn")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_COAST = (By.CSS_SELECTOR, ".product_main > .price_color")
    ITEM_IN_CART_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    ITEM_IN_CART_NAME = (By.CSS_SELECTOR, "#messages strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".page_inner a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    AUTHORIZATION_LINK = (By.ID, "login_link")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn-block")


#Проверочный тег - "#product_description h2"