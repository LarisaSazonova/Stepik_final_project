from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "There should be 'login' in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
        
    def register_new_user(self, email, password):
        email_field= self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
        email_field.send_keys(email)

        password1_field = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
        password1_field.send_keys(password)

        password2_field = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
        password2_field.send_keys(password)

        register_button = self.browser.find_element(By.CSS_SELECTOR, "#register_form > button")
        register_button.click()








