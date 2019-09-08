import pytest
from oxwall_site_model import OxwallSite

#@pytest.mark.skip("doent work teardown")
def test_login_using_page_object(oxwall_app,driver, user,signed_in_user):

    #Ensure that DASHBOARD is title if page
    assert oxwall_app.dash_page.is_this_page()

    #Ensure that in page present 2 icons on rigth top corner
    assert oxwall_app.dash_page.is_logged_in()

    #Ensure that name in icon and in file are the same
    assert oxwall_app.dash_page.user_menu.text == user.real_name