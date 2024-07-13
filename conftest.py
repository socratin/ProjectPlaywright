import pytest
from playwright.sync_api import sync_playwright

from pages.collection import CollectionPage
from pages.create_account import CreateAccount
from pages.sale import Sale


@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def CreatePageAccount(browser):
    page = browser.new_page()
    return CreateAccount(page)

@pytest.fixture(scope='function')
def SalePage(browser):
    page = browser.new_page()
    return Sale(page)

@pytest.fixture(scope='function')
def Collection(browser):
    page = browser.new_page()
    return CollectionPage(page)

