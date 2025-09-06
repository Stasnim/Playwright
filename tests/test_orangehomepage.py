import time
from playwright.sync_api import Page, expect
from pages.orange_login_page import LoginPage
from pages.orangehrm_home_page import HomePage

def test_example(page:Page)-> None:
    """"page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("textbox", name="Performance").click()
    page.get_by_role("textbox", name="Upgrade").click()
    page.get_by_role("link", name="Dashboard").click()
    page.get_by_role("button", name="Dashboard").click()"""

    login_page= LoginPage(page)
    home_page= HomePage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()


    home_page.is_upgrade_button_visible()
    home_page.click_performance()
    home_page.click_dashboard()




