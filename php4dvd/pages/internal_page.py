from pages.page import Page
from selenium.webdriver.common.by import By


class InternalPage(Page):

    @property
    def settings_dropdown_toggle(self):
        return self.driver.find_element(By.CLASS_NAME, "dropdown-toggle")

    @property
    def user_management_in_dropdown_menu(self):
        element_dropdown_menu = self.driver.find_element(By.CLASS_NAME, "dropdown-menu")
        a_element = element_dropdown_menu.find_element(By.CSS_SELECTOR, "[href='http://php4dvd/?go=users']")
        return a_element

    @property
    def logout_in_dropdown_menu(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-type='logout']")

    @property
    def сonfirm_button_in_modal_dialog_window(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(2)")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "[title='Home']"))
