from model.user import User
from conftest import app


def test_add_user(app):
    new_user = User.random()
    app.login(User.Admin())
    # app.ensure_login_as(User.Admin())
    app.add_user(new_user)
    assert app.is_user_management_page()
    app.logout()
    app.login(new_user)
    assert app.is_logged_in()

    # app.logout()
    # app.login(new_user)
    # assert app.is_logged_in()
    # app.logout()
