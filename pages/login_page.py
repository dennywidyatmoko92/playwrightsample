from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#active-login input[type='email']")
        self.password_input = page.locator("#active-login input[type='password']")
        self.login_button = page.get_by_role("button", name="Log in")
        self.login_link = page.get_by_text("login", exact=True)
        self.error_message = page.get_by_text("An account with this email")
