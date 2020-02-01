from selenium.webdriver.common.by import By
from locators import MainPageLocators
from locators import LoginPageLocators
from .base_page import BasePage
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Reg form is not presented"
        assert True

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGNAME)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REGPASS)
        input_password.send_keys(password)
        input_confpass = self.browser.find_element(*LoginPageLocators.REGCONF)
        input_confpass.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGBUTTON)
        reg_button.click()
        time.sleep(2)

    def new_user_message(self):
        assert self.is_element_present(*LoginPageLocators.REGISTERED), "New user is registered"
        assert True