from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    OFF_PLAN_MENU = (By.CSS_SELECTOR, 'address.menu-twobutton')

    def open_main_page(self):
        self.open_url('https://soft.reelly.io/')
        self.verify_url('https://soft.reelly.io/')
        sleep(4)

    def click_off_plan_menu(self):
        self.click(*self.OFF_PLAN_MENU)
