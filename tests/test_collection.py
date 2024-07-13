def test_view_card_items(Collection):
    Collection.open_page()
    Collection.check_counter_items_on_page()


def test_count_view(Collection):
    Collection.open_page()
    Collection.check_visible_counter_items_on_page()


def test_view_button_cart_compare_like(Collection):
    Collection.open_page()
    Collection.go_to_card_item()
    Collection.check_visible_name_item()
