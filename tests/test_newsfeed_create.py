from oxwall_site_model import OxwallSite
from value_models.status import Status
import pytest
from data.status_data import status_data


@pytest.mark.parametrize("status_text", status_data)
def test_add_text_status(driver, signed_in_user, status_text):
    status = Status(text=status_text, user=signed_in_user)
    app = OxwallSite(driver)
    # old_status_list = app.dash_page.status_list
    assert app.dash_page.status_text_field.placeholder == "What’s happening?"
    app.dash_page.status_text_field.input(status.text)
    app.dash_page.send_button.click()
    app.dash_page.wait_until_new_status_appeared()
    # new_status_list = app.dash_page.status_list
    new_status = app.dash_page.status_list[0]
    assert new_status.text == status.text
    assert new_status.user == signed_in_user.real_name
    assert new_status.time == "within 1 minute"


    # Verification that new status with this text appeared
    # text_elements = app.get_newsfeed_list()
    # newsfeed_users = app.get_newsfeed_users()
    # newsfeed_times = app.get_newsfeed_times()
    # assert text_elements[0].text == status.text
    # assert newsfeed_users[0].text == status.user.real_name
    # assert newsfeed_times[0].text == "within 1 minute"