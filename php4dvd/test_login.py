from selenium import webdriver
from selenium_fixture import app
from model.user import User
import time


def test_login_with_valid_credentials(app):
    app.go_to_home_page()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()
    assert app.is_not_logged_in()


def test_login_with_invalid_credentials(app):
    app.go_to_home_page()
    app.login(User.random())
    assert app.is_not_logged_in()
