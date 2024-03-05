import allure
from allure_commons.types import AttachmentType
from pages.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import time


class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    PROFILE_DROPDOWN = ("xpath", "//span[@class='oxd-userdropdown-tab']")
    LOG_OUT = ("xpath", "//a[@href='/web/index.php/auth/logout']")
    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")

    @allure.step("Pressing 'Logout' button")
    def press_logout_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOG_OUT)).click()

    @allure.step("Opening user profile dropdown")
    def open_drop_down_profile_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_DROPDOWN)).click()

    def log_out(self):
        self.open_drop_down_profile_menu()
        self.press_logout_button()
        time.sleep(5)
        self.make_screenshot('Logged out - DONE')

    @allure.step("Opening 'My info' section")
    def click_my_info_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()

