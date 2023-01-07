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

    # if request.url == 'https://ipamm.ale.local/pam/idp/External/Challenge?scheme=Negotiate':
    #     request.headers['Authorization'] = f'Basic {auth}'
    #     print(request.headers['Authorization'])
    #     pritnt()






def test_setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome()

    time.sleep(2)
    # driver.request_interceptor = interceptor
    driver.get("https://ipamm.ale.local/pam/idp/Account/Login")
    autoit.win_wait_active("",30)
    autoit.send("Admin{TAB}")
    autoit.send("QWEqwe123{Enter}")


    driver.maximize_window()

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
