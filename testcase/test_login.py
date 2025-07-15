import sys
import os

# Tambahkan path ke root agar bisa import logic.*
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from playwright.sync_api import sync_playwright
from logic.login_logic import (
    click_login_link,
    input_email,
    input_password,
    click_login_button,
    verify_login_error_visible
)
from logic.common_logic import go_to_login_page  # ✅ diperbaiki sesuai lokasi fungsi

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        yield page
        browser.close()

def test_invalid_login(page):
    go_to_login_page(page)
    click_login_link(page)
    input_email(page, "denypekaz1@krafthaus.coid")
    input_password(page, "kjkszpj123456")
    click_login_button(page)
    verify_login_error_visible(page)
