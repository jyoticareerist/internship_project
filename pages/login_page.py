from selenium.webdriver.common.by import By

from pages.base_page import Page


class LoginPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input#email-2[type="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input#field[type="password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'a.login-button[wized="loginButton"]')

    def login_and_redirect(self):
        self.verify_url('https://soft.reelly.io/sign-in')
        self.input("joooz786@gmail.com", *self.EMAIL_FIELD)
        self.input("@Seven86", *self.PASSWORD_FIELD)
        self.click(*self.LOGIN_BTN)
        self.verify_url('https://soft.reelly.io/')
