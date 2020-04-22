from pages import AdminAutorizationPage
from data_for_test import TestData


class TestAdminSmoke:

    def test_admin_autorization(self, browser):
        bro = browser
        AdminAutorizationPage(bro).auth_by_admin(TestData.ADMIN_LOGIN, TestData.ADMIN_PASSWORD)
        AdminAutorizationPage(bro).located_admin_menu_page()
