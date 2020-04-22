from locators import AdminAutorization
from locators import AdminMenu
from pages.BasePage import BasePage


class AdminAutorizationPage(BasePage):


    def auth_by_admin(self, email, password):
        self.driver.get("http://attestation.test/admin")
        self._input(AdminAutorization.email_field, email)
        self._input(AdminAutorization.password_field, password)
        self._click(AdminAutorization.submit_button)

    def located_admin_menu_page(self):
        self._wait_for_visible(AdminMenu.account_dropdown)
