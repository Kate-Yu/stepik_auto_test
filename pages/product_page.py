from .base_page import BasePage
from selenium.webdriver.common.by import By
from locators import MainPageLocators
from locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
            self.add_product()
            self.should_be_product_in_basket()
            self.should_be_product_name()
            self.should_item_name_match()
            self.should_price_name_match()       

    def add_product(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_LINK).click(), "Button is not presented"

    def should_item_name_match(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        actual_item = item_name.text
        added_item_name = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME)
        added_item = added_item_name.text
        assert actual_item == added_item, "No match"

    def should_item_price_match(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        actual_price = item_price.text
        added_item_price = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_PRICE)
        added_price = added_item_price.text
        assert actual_price == added_price, "No match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is disappeared, but should not be"
