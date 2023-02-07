import pytest
import time
import json
from seleniumwire import webdriver
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import base64
import autoit


def test_setup():
    # options = webdriver.ChromeOptions()
    # options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome()

    # driver = webdriver.Firefox()

    time.sleep(2)
    # driver.request_interceptor = interceptor
    driver.get("https://redos-ipamm.pam-ad1.local/mc")
    driver.maximize_window()
    driver.implicitly_wait(2)
    username = driver.find_element(By.ID, 'Username')
    username.send_keys('Admin')
    password = driver.find_element(By.ID, 'Password')
    password.send_keys("QWEqwe123")
    button_login = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
    button_login.click()
    link_resources = driver.find_element(By.ID, 'icon-filled-server')
    link_resources.click()
    time.sleep(100)

    for request in driver.requests:
        print(request.headers)
        print(request.url)
        if request.response:
            print(
                # request.url,
                request.response
            )

    time.sleep(100)
    driver.quit()

##Trash


# driver.implicitly_wait(0.5)
#
#
# basic_auth = [
#     "browserstack_executor", {
#         "action": "sendBasicAuth",
#         "arguments": {
#             "timeout": "<time in milliseconds>",
#             "username": "admin",
#             "password": "QWEqwe123",
#         }
#     },
# ]
#
# y = json.dumps(basic_auth)
#
# driver.execute_script( y )
