def test_choose_woomen_deals_category(SalePage):
    SalePage.open_page()
    SalePage.choose_category_women_hoddies_and_swetear()
    SalePage.check_coun_category()


def test_go_to_main_page(SalePage):
    SalePage.open_page()
    SalePage.go_to_main_page()
    SalePage.check_current_url(SalePage.base_url)


def test_view_promo_block(SalePage):
    SalePage.open_page()
    SalePage.check_visible_promo_block()
