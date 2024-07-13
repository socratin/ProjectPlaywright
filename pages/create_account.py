from locators.create_account_locators import CreateAccountLocators
from pages.base_page import BasePage


class CreateAccount(BasePage):
    page_url = "/customer/account/create/"

    def check_name_page(self):
        self.check_visible_element(CreateAccountLocators.field_name_page)

    def fill_email(self, email):
        self.find_element(CreateAccountLocators.input_email).fill(email)

    def press_button_create_account(self):
        self.find_element(CreateAccountLocators.button_create).click()

    def check_visible_error_email(self):
        self.check_visible_element(CreateAccountLocators.error_email)

    def fill_password(self, password):
        self.find_element(CreateAccountLocators.input_password).fill(password)

    def check_visible_error_password(self):
        self.check_visible_element(CreateAccountLocators.error_password)
