from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".btn-group")
    EMPTY = (By.CSS_SELECTOR, ".basket-items")
    TEXT_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    USERNAME = (By.CSS_SELECTOR, "#id_login-username.form-control")
    USERPASS = (By.CSS_SELECTOR, "#id_login-password.form-control")
    REGNAME = (By.CSS_SELECTOR, "#id_registration-email.form-control")
    REGPASS = (By.CSS_SELECTOR, "#id_registration-password1.form-control")
    REGCONF = (By.CSS_SELECTOR, "#id_registration-password2.form-control")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")
    REG_FORM = (By.CSS_SELECTOR, "#register_form.well")
    REGBUTTON = (By.CSS_SELECTOR, "#register_form > button")
    REGISTERED = (By.CSS_SELECTOR, "#messages > div> .alertinner")

class ProductPageLocators():
    PRODUCT_LINK  = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE = (By.CSS_SELECTOR, "#messages")
    ITEM_NAME = (By.CSS_SELECTOR, ".col-sm-6 > h1")
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p.price_color")
    ADDED_ITEM_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
