from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from support.logger import logger


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)
        logger.info(f'Opening url {url}')

    def get_current_url(self):
        return self.driver.current_url

    def verify_url(self, expected_url):
        current_url = self.get_current_url()
        self.driver.wait.until(
            EC.url_to_be(expected_url),
            message=f'Expected URL({expected_url}) does not match the Actual URL({current_url})'
        )
        logger.info(f"Current URL: {self.get_current_url()}")

    def verify_partial_url(self, expected_url):
        current_url = self.get_current_url()
        self.driver.wait.until(
            EC.url_contains(expected_url),
            message=f'Expected URL({expected_url}) does not match the Actual URL({current_url})'
        )

    def verify_exact_match(self, expected_text, actual_text):
        assert expected_text == actual_text, \
            f'Expected({expected_text}) is not present in Actual({actual_text})'

    def wait_until_visible(self, *locator):
        logger.info(f'{locator} wait until visible')
        self.wait.until(
            EC.visibility_of_element_located(locator),
            f"{locator} not present!"
        )

    def click(self, *locator):
        self.driver.find_element(*locator).click()
        logger.info(f'Clicking the element: {locator}')

    def input(self, text, *locator):
        logger.info(f'Input {text} in element {locator}')
        self.driver.find_element(*locator).send_keys(text)

    def find_element(self, *locator):
        logger.info(f'Searching for element {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f'Searching for elements {locator}')
        return self.driver.find_elements(*locator)

    def wait_until_all_elements_present(self, *locator):
        logger.info(f'{locator} wait until all elements present')
        self.wait.until(
            EC.presence_of_all_elements_located(locator),
            f"{locator} not present!"
        )
