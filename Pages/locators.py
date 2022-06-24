from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form.well")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")