def test_open_page_create_new_account(CreatePageAccount):
    CreatePageAccount.open_page()
    CreatePageAccount.check_name_page()


def test_invalid_input_email(CreatePageAccount):
    CreatePageAccount.open_page()
    CreatePageAccount.fill_email("test")
    CreatePageAccount.press_button_create_account()


def test_invalid_input_password(CreatePageAccount):
    CreatePageAccount.open_page()
    CreatePageAccount.fill_password("123")
    CreatePageAccount.press_button_create_account()
    CreatePageAccount.check_visible_error_password()
