
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(playwright):
    # Force language to English
    context = playwright.chromium.launch_persistent_context(
        user_data_dir="/tmp/test-user-data-dir",  # use a temp path
        headless=False,
        locale="en-US"
    )
    page = context.pages[0] if context.pages else context.new_page()
    yield page
    context.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


