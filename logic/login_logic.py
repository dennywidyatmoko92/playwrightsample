from pages.login_page import LoginPage

def click_login_link(page):
    login_page = LoginPage(page)
    login_page.login_link.click()

def input_email(page, email):
    login_page = LoginPage(page)
    login_page.email_input.fill(email)

def input_password(page, password):
    login_page = LoginPage(page)
    login_page.password_input.fill(password)

def click_login_button(page):
    login_page = LoginPage(page)
    login_page.login_button.click()

def verify_login_error_visible(page):
    login_page = LoginPage(page)
    assert login_page.error_message.is_visible()
