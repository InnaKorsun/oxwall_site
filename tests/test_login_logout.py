import pytest
from oxwall_site_model import OxwallSite


def test_login_using_page_object(driver, user, logout):

    app = OxwallSite(driver)
    app.main_page.sign_in_click()
    assert app.sign_in_page.is_this_page()
    app.sign_in_page.username_field.input(user.username)
    app.sign_in_page.password_field.input(user.password)
    app.sign_in_page.submit_form()
    assert app.dash_page.is_this_page()
    assert app.dash_page.is_logged_in()
    assert app.dash_page.user_menu.text == user.real_name