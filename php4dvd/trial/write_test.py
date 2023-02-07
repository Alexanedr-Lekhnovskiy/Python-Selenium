import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_setup():
    driver = webdriver.Firefox()
    driver.get("https://www.novsu.ru/")
    par = driver.find_element(By.XPATH, "/html/body/")
    # par = driver.find_element(By.LINK_TEXT, "Корпоративный портал")
    par.click()
    driver.quit()


    #driver.quit()
