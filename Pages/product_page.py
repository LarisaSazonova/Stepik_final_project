from math import prod
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        
    def check_message_appeared_when_product_item_added_to_basket(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_ALERT)
        assert "has been added to your basket" in success_message.text, "No message about adding product item to the basket"

    def validate_product_name_in_message(self):
        product_name_in_success_message = self.browser.find_element(*ProductPageLocators.PRODCUT_NAME_IN_SUCCESS_MESSAGE_ALERT)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name_in_success_message.text == product_name.text, "Product name in the message is not equal product name added to basket"

    def check_basket_total_message_appeared(self):
        basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_ALERT)
        assert "Your basket total is now" in basket_total_message.text, "No message about basket total"

    def validate_basket_total_amount(self):
        price_in_basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_IN_BASKET_MESSAGE_ALERT)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert price_in_basket_total_message.text == product_price.text, "Basket total is not equal to product price"

