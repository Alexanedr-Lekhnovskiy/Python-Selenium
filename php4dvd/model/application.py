from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class Application(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.base_url = base_url

    def go_to_home_page(self):
        self.driver.get(self.base_url)

    def login(self, user):
        self.driver.find_element(By.ID, "password").send_keys(user.username)
        self.driver.find_element(By.ID, "username").send_keys(user.password)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-block").click()

    def logout(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div[3]/ul/li[2]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div[3]/ul/li[2]/ul/li[3]/a").click()
        self.driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(2)").click()

    def is_logged_in(self):
        driver = self.driver
        try:
            self.wait.until(presence_of_element_located((By.CLASS_NAME, 'fa-plus-circle')))
            return True
        except WebDriverException:
            return False

    def is_not_logged_in(self):
        driver = self.driver
        try:
            self.wait.until(presence_of_element_located((By.CLASS_NAME, 'login-box-body')))
            return True
        except WebDriverException:
            return False