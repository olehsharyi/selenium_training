import allure

from tests.base_test import BaseTest


@allure.feature("Smoke Tests")
class TestLoginLogout(BaseTest):

    @allure.story('Login process')
    def test_login(self, proceed_login):
        assert self.login_page.current_url() == self.links.DASHBOARD_PAGE

    @allure.story('Logout process')
    def test_logout(self, proceed_login):
        self.dashboard_page.log_out()
        assert self.login_page.current_url() == self.links.LOGIN_PAGE

    @allure.story('Search process')
    def test_search(self, proceed_login):
        self.home_page.search_query('Admin')



