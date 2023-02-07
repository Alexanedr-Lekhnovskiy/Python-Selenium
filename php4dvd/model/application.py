from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.internal_page import InternalPage
from pages.user_management_page import UserManagementPage


class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 10)

        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.user_management_page = UserManagementPage(driver, base_url)

    def login(self, user):
        lp = self.login_page

        lp.username_field.clear()
        lp.username_field.send_keys(user.username)
        lp.password_field.clear()
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def logout(self):
        ip = self.internal_page
        ip.settings_dropdown_toggle.click()
        ip.logout_in_dropdown_menu.click()
        ip.сonfirm_button_in_modal_dialog_window.click()

    def ensure_logout(self):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "[title='Settings'], #loginform ")))
        if element.tag_name == "i":
            self.logout()

    # TODO
    # def ensure_login_as(self, user):
    #     element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "[title='Settings'], #loginform ")))
    #     if element.tag_name == "i":
    #         if self.is_logged_in_as(user):
    #             return
    #         else:
    #             self.logout()
    #     self.login(user)

    def is_logged_in(self):
        return self.internal_page.is_this_page

    def is_not_logged_in(self):
        return self.login_page.is_this_page

    def add_user(self, user):
        ip = self.internal_page
        ip.settings_dropdown_toggle.click()
        ip.user_management_in_dropdown_menu.click()

        ump = self.user_management_page
        ump.user_form.is_this_page

        ump.user_form.username_field.send_keys(user.username)
        ump.user_form.email_field.send_keys(user.email)
        ump.user_form.password_field.send_keys(user.password)
        ump.user_form.password_again_field.send_keys(user.password)

        # TODO
        # ump.role

        ump.user_form.submit_button.click()

    def is_user_management_page(self):
        return self.user_management_page.is_this_page
