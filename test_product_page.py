from selenium.webdriver.common.by import By
from .Pages.product_page import ProductPage

# Проверяем сценарий добавления товара в корзину со страницы товара. 
# Ожидаемый результат: 
# 1)Cообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
# 2)Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    #для получения проверочного кода
    page.solve_quiz_and_get_code()

    page.check_message_appeared_when_product_item_added_to_basket()

    page.validate_product_name_in_message()

    page.check_basket_total_message_appeared()

    page.validate_basket_total_amount()

