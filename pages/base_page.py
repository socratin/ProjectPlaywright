from playwright.sync_api import Page, expect

from locators.sale_locators import SaleLocators


class BasePage():
    base_url = "https://magento.softwaretestingboard.com"
    page_url = ""

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(f"{self.base_url}/{self.page_url}")

    def check_visible_element(self, selector: str):
        expect(self.page.locator(selector)).to_be_visible()

    def find_element(self, selector: str):
        return self.page.locator(selector)

    def find_elements(self, selector: str):
        return self.page.query_selector_all(selector)

    def go_to_main_page(self):
        self.find_element(SaleLocators.logo).click()

    def check_current_url(self, url: str):
        expect(self.page).to_have_url(self.base_url+"/")

    def move_cursor_to_element(self, selector: str):
        self.page.locator(selector).hover()
