from oxwall_site_model import OxwallSite
from selenium.webdriver.remote.webelement import WebElement
from value_models.status import Status
import pytest
from data.status_data import status_data

#Test to add newsfeed
#@pytest.mark.skip("doent work teardown")
@pytest.mark.parametrize("status_text",status_data)
def test_add_text_status(oxwall_app,db,user_full_info ,signed_in_user,status_text ):

    #create test status (text present in status_data.json)
    status = Status(text=status_text, user=user_full_info.username)

    # ensure that What happenning present in page
    assert oxwall_app.dash_page.status_text_field.placeholder == "What’s happening?"

    #Enter text to status text
    oxwall_app.dash_page.status_text_field.input(status.text)
    oxwall_app.dash_page.send_button.click()
    oxwall_app.dash_page.wait_until_new_status_appeared()

    #Get just created status(by web form)
    new_status = oxwall_app.dash_page.status_list[0]

    #Ensure that text,time are the same(from web form and status that we created below)
    assert new_status.text == status.text
    assert new_status.time == "within 1 minute"

    # Get status from datebase
    status_from_db = db.get_last_text_status()

    #Ensure that text,author is yhe same in datd base and webform
    assert new_status.text == status_from_db.text
    assert status_from_db.user==new_status.user
    #Optionally - teardown  - delete status
    #db.delete_status_by_id(status_from_db.id)



