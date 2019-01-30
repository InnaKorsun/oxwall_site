from oxwall_site_model import OxwallSite
from selenium.webdriver.remote.webelement import WebElement
from value_models.status import Status
import pytest
from data.status_data import status_data


@pytest.mark.parametrize("status_text",status_data)
def test_add_text_status(driver, signed_as_admin , oxwall_app, status_text,db):

    status = Status(text=status_text, user=signed_as_admin)


    assert oxwall_app.dash_page.status_text_field.placeholder == "What’s happening?"

    oxwall_app.dash_page.status_text_field.input(status.text)
    oxwall_app.dash_page.send_button.click()
    oxwall_app.dash_page.wait_until_new_status_appeared()
    new_status = oxwall_app.dash_page.status_list[0]

    assert new_status.text == status.text
    assert new_status.time == "within 1 minute"
    status_from_db = db.get_last_text_status()

    assert status.text == status_from_db.text
    db.delete_status_by_id(status_from_db.id)



    # Verification that new status with this text appeared
    # text_elements = app.get_newsfeed_list()
    # newsfeed_users = app.get_newsfeed_users()
    # newsfeed_times = app.get_newsfeed_times()
    # assert text_elements[0].text == status.text
    # assert newsfeed_users[0].text == status.user.real_name
    # assert newsfeed_times[0].text == "within 1 minute"