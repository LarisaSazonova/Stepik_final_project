from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form.well")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    SUCCESS_MESSAGE_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    PRODUCT_NAME = (By.CSS_SELECTOR,"#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    BASKET_TOTAL_MESSAGE_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(3)")
    PRODUCT_PRICE = (By.CSS_SELECTOR,"#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    