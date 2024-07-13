from locators.store_collection_locators import CardItem, StoreCollectionLocators
from pages.base_page import BasePage


class CollectionPage(BasePage):
    page_url = "/collections/eco-friendly.html"

    def check_counter_items_on_page(self):
        items = self.find_elements(StoreCollectionLocators.item_card)
        assert len(items) == 13

    def check_visible_counter_items_on_page(self):
        assert self.find_element(StoreCollectionLocators.field_amount_items)

    def go_to_card_item(self):
        items = self.find_elements(StoreCollectionLocators.items_list)
        items[0].hover()
        items[0].click()

    def check_visible_name_item(self):
        assert self.find_element(CardItem.item_name)
