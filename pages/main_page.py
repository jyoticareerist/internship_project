from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    OFF_PLAN_MENU = (By.CSS_SELECTOR, 'address.menu-twobutton')
    OFF_PLAN_MENU_MOBILE = (By.CSS_SELECTOR, 'div[wized="mobileMenuForVerifiedUsers"] a.menu-link[href="/off-plan"]')

    def open_main_page(self):
        self.open_url('https://soft.reelly.io/')
        sleep(4)

    def click_off_plan_menu(self):
        self.click(*self.OFF_PLAN_MENU)

    def click_off_plan_menu_mobile(self):
        self.click(*self.OFF_PLAN_MENU_MOBILE)
