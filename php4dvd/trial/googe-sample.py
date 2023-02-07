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


class TestSamsapletext():
    def setup_method(self, method):
        ##local-Test
        # self.driver = webdriver.Firefox()
        # self.vars = {}

        ##Remote-Test
        # self.driver = webdriver.Remote('http://10.11.2.9:4444', webdriver.DesiredCapabilities.CHROME)
        self.driver = webdriver.Remote(
            command_executor='http://10.11.2.9:4444',
            options=webdriver.ChromeOptions()
        )

        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_samsapletext(self):
        self.driver.get("https://www.google.com/")
        self.driver.set_window_size(1134, 755)
        self.driver.find_element(By.NAME, "q").click()
        self.driver.find_element(By.NAME, "q").click()
        self.driver.find_element(By.NAME, "q").send_keys("sample text")
