import allure
from pages.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE
    TARGET_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
    PROFILE_DROPDOWN = ("xpath", "//span[@class][1]")
    LOG_OUT = ("xpath", "")

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        time.sleep(2)
        self.make_screenshot('Login - DONE')

    def login_in(self, login, password):
        self.open()
        self.enter_login(login)
        self.enter_password(password)
        self.click_submit_button()
        self.wait_for_url_to_be()




