from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page
from support.logger import logger


class ProductDetailsPage(Page):
    VISUALIZATION_TABS = (By.CSS_SELECTOR, '.tabs-menu-project a')
    SELECTED_TAB = (By.CSS_SELECTOR, '.tabs-menu-project a[aria-selected="true"]')
    VISUALIZATION_OPTIONS = ['Architecture', 'Lobby', 'Interior']

    def verify_visualization_options(self):
        self.verify_partial_url('project/general?projectid=')
        # sleep(5)
        self.wait_until_all_elements_present(*self.VISUALIZATION_TABS)
        tab_options = []
        visualization_tabs = self.find_elements(*self.VISUALIZATION_TABS)
        for tab in visualization_tabs:
            tab_text = tab.find_element(By.CSS_SELECTOR, 'div div').text
            tab_options.append(tab_text)
        assert sorted(tab_options) == sorted(self.VISUALIZATION_OPTIONS), \
            f'All Tabs are not present! Expected({self.VISUALIZATION_OPTIONS}) vs Actual({tab_options})'
        logger.info(f'Tab Elements: {tab_options} verified against {self.VISUALIZATION_OPTIONS} - all are present')

    def verify_visualization_clickable(self):
        visualization_tabs = self.find_elements(*self.VISUALIZATION_TABS)
        for tab in visualization_tabs:
            tab_text = tab.find_element(By.CSS_SELECTOR, 'div div').text
            if not tab_text:
                tab_text = tab.find_element(By.CSS_SELECTOR, 'div').text
            print(f'Tab text: {tab_text}')
            tab.click()
            selected_tab_text = self.find_element(*self.SELECTED_TAB).find_element(By.CSS_SELECTOR, 'div div').text
            self.verify_exact_match(tab_text, selected_tab_text)
            logger.info(f'"{tab_text}" Click verified')
