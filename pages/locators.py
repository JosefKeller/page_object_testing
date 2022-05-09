from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators():
    ALERT_SUCCESS = (By.CLASS_NAME, "alert-success")
    ALERT_INFO = (By.CLASS_NAME, "alert-info")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")


class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
