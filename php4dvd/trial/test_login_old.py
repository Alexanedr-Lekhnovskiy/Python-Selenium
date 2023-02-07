# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTest1():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

        # self.driver = webdriver.Remote('http://10.11.2.12:4444', webdriver.DesiredCapabilities.CHROME)
        # self.vars = {}
        # self.base_url = "http://10.11.2.20/"


    def teardown_method(self, method):
        self.driver.quit()

    def test_test1(self):
        self.driver.get(self.base_url + "/php4dvd/")
        self.driver.set_window_size(1134, 750)
        self.driver.find_element(By.ID, "password").send_keys("admin")
        self.driver.find_element(By.ID, "username").send_keys("admin")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-block").click()