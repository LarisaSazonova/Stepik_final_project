from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def check_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY, 5), "There are items to buy in basket, but should not be"

    def check_message_basket_is_empty_appeared(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "No message that basket is empty"

