from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.create_account import CreateAccount


def test(browser):
    page = browser.new_page()
    test_page = CreateAccount(page)
    test_page.open_page()
