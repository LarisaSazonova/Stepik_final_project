import pytest
from .Pages.product_page import ProductPage
from .Pages.basket_page import BasketPage 

# Проверяем сценарий добавления товара в корзину со страницы товара. 
# Ожидаемый результат: 
# 1)Cообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
# 2)Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()  #для получения проверочного кода
    page.check_message_appeared_when_product_item_added_to_basket()
    page.validate_product_name_in_message()
    page.check_basket_total_message_appeared()
    page.validate_basket_total_amount()

# Тот же тест, но с параметризацией (проверяем 10 промо-страниц)

@pytest.mark.parametrize('promo_offer', ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", 
"promo=offer4", "promo=offer5", "promo=offer6", pytest.param("promo=offer7", marks=pytest.mark.xfail), "promo=offer8", "promo=offer9"])
@pytest.mark.skip
def test_guest_can_add_product_to_basket_2(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()  #для получения проверочного кода
    page.check_message_appeared_when_product_item_added_to_basket()
    page.validate_product_name_in_message()
    page.check_basket_total_message_appeared()
    page.validate_basket_total_amount()


# Проверки, что некоторые элементы отсутствуют на странице
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()  #для получения проверочного кода
    page.check_success_message_didnt_appear()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.check_success_message_didnt_appear()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()  #для получения проверочного кода
    page.check_success_message_disappears_after_adding_product_to_basket()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_is_empty()
    basket_page.check_message_basket_is_empty_appeared()

    