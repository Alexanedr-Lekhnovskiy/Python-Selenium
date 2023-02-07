import pytest
import time
import json
from seleniumwire import webdriver
# from selenium import webdriver
import requests
from requests.auth import HTTPBasicAuth

res = requests.get('https://ipamm.ale.local/pam/mc', auth=HTTPBasicAuth('admin', 'QWEqwe123'), verify=False)
print(res.content)

# def test_setup():
#
#
#     driver = webdriver.Chrome()
#     driver.get("https://ipamm.ale.local/pam/mc")
#     driver.maximize_window()
#
#     for request in driver.requests:
#         print(
#             request.url
#         )
#
#     time.sleep(100)
#     driver.quit()
