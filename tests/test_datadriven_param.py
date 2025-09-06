import time

import pytest
from playwright.sync_api import Page,Playwright, expect

@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin", "admin123"),
        ("user1", "password")
    ]
)


def test_example(page:Page, username, password)-> None:
    page.set_default_timeout(1000)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login?lang=en")
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()

    page.get_by_role("link", name="Performance").click()

    page.context.close()