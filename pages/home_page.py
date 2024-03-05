import allure
from pages.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE

    SEARCH_FIELD = ("xpath", "//input[@placeholder='Search']")

    def search_query(self, query):
        with allure.step(f' Sending {query} to Search placeholder'):
            search_field = self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD))
            search_field.send_keys(query)

        with allure.step(f'Verifying placeholder value to be {query}'):
            placeholder_value = search_field.get_attribute('value')
            assert placeholder_value == query

        self.make_screenshot('Done')





