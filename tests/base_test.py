import pytest
from config.data import Data
from config.links import Links
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.home_page import HomePage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest:
    data: Data
    login_page: LoginPage
    links: Links
    dashboard_page: DashboardPage
    home_page: HomePage

    @pytest.fixture(autouse=True)
    def setup(self, request):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument('--headless')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.links = Links()
        request.cls.login_page = LoginPage(driver)
        request.cls.home_page = HomePage(driver)
        request.cls.dashboard_page = DashboardPage(driver)

        yield driver

        driver.quit()

    @pytest.fixture
    def proceed_login(self, request):
        login_page = request.cls.login_page
        login_page.login_in(login=request.cls.data.LOGIN, password=request.cls.data.PASSWORD)
        yield login_page
