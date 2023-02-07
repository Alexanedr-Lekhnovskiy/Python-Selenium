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

auth = (
    base64.encodebytes('locaAdmin : QWEqwe123'.encode())
        .decode()
        .strip()
)


def interceptor(request):
    if request.host == 'ipamm.ale.local':
        request.headers['Authorization'] = f'Basic {auth}'
        print(request.headers['Authorization'])


def test_setup():
    # В конфиге idp нужно настроить
    #   "DirectoryMechanism": "Local",
    #   "Authentication": "Ldap",
    #
    #   Также ещё придется отдельно настроить секцию LDAP
    #   "Ldap": {
    #     "Domain": "pam-ad1.local",
    #     "Username": "pamadmin",
    #     "Password": "QWEqwe123",
    #     "Port": 636,
    #     "SecureSocketLayer": true,
    #     "AuthType": "Basic"
    #   },

    username = 'admin'
    password = 'QWEqwe123'
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()

    time.sleep(2)
    # driver.request_interceptor = interceptor
    # driver.get("https://ipamm.pam-ad1.local/pam/idp/Account/Login")
    driver.get("https://pamadmin:QWEqwe123@ipamm.pam-ad1.local/pam/mc")
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    # autoit.win_wait_active("",30)
    # autoit.send(f"{username}""{TAB}")
    # autoit.send(f"{password}""{Enter}")
    # driver.get('https://ipamm.pam-ad1.local/pam/mc')
    # link_resources = driver.find_element(By.ID, 'icon-filled-server')
    # link_resources.click()

    for request in driver.requests:
        print(request.headers)
        print(request.url)
        if request.response:
            print(
                # request.url,
                request.response
            )

    time.sleep(2)
    driver.quit()
