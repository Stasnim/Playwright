import time
import pytest
from playwright.sync_api import sync_playwright

def test_run(browser_name):
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        browser.close()