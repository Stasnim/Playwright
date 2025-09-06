import time

import pytest
from playwright.sync_api import Page,Playwright, expect
import csv

def load_csv(filename: str) -> list:
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Optional: skip header
        for row in reader:
            data.append(tuple(row))
    return data
# @pytest.mark.parametrize("username, password", get_csv_data())
def get_json_data() -> list:
    import json
    with open("./test_data/data.json", "r") as file:
        data = json.load(file)
    return [(item['username'], item['password']) for item in data]
@pytest.mark.parametrize("username, password", get_json_data())

def test_example(page:Page, username, password)-> None:

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login?lang=en")
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()

    page.get_by_role("link", name="Performance").click()
    page.set_default_timeout(5000)
    page.context.close()