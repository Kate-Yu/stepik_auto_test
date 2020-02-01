import pytest
import time
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.product_page import ProductPage

@pytest.mark.parametrize('links', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail), "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])


def test_guest_can_add_product_to_basket(browser, links):
    links = f"{links}"
    page = ProductPage(browser, links)
    page.open()
    page.add_product()
    time.sleep(2)
    page1 = BasePage(browser, links)
    page1.solve_quiz_and_get_code()
    page.should_item_name_match()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    page.should_disappear_success_message()