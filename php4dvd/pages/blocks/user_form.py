from pages.page import Page
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class UserForm(Page):

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CLASS_NAME, "col-md-4"))

    @property
    def username_field(self):
        return self.driver.find_element(By.ID, "username")

    @property
    def email_field(self):
        return self.driver.find_element(By.ID, "email")

    @property
    def password_field(self):
        return self.driver.find_element(By.ID, "password")

    @property
    def password_again_field(self):
        return self.driver.find_element(By.ID, "password2")

    @property
    def submit_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name='submit']")
