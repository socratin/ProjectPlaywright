from locators.sale_locators import SaleLocators
from pages.base_page import BasePage


class Sale(BasePage):
    page_url = "/sale.html"

    def choose_category_women_hoddies_and_swetear(self):
        categories = self.find_elements(SaleLocators.category_hoddies_and_sweaters)
        categories[0].click()

    def check_coun_category(self):
        categories = self.find_elements(SaleLocators.name_category)
        assert len(categories) == 3

    def check_visible_promo_block(self):
        assert self.find_element(SaleLocators.block_promo)