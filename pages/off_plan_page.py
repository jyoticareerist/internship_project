from selenium.webdriver.common.by import By

from pages.base_page import Page


class OffPlanPage(Page):
    PRODUCT_CARDS = (By.CSS_SELECTOR, '[wized="projectsListing"] [wized="cardOfProperty"]')
    FIRST_PRODUCT_CARD = (By.CSS_SELECTOR, '[wized="cardOfProperty"][style="display: block;"]')

    def verify_off_plan_page(self):
        self.verify_url('https://soft.reelly.io/off-plan')

    def click_first_product(self):
        self.wait_until_visible(*self.FIRST_PRODUCT_CARD)
        self.click(*self.PRODUCT_CARDS)

