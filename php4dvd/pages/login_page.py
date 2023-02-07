from pages.page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):

    @property
    def username_field(self):
        return self.driver.find_element(By.ID, "username")

    @property
    def password_field(self):
        return self.driver.find_element(By.ID, "password")

    @property
    def submit_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".btn-block")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CLASS_NAME, 'login-box-body'))
