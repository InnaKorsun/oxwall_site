from oxwall_site_model import OxwallSite
from value_models.status import Status
import pytest
from data.status_data import status_data


#@pytest.mark.parametrize("status_text", status_data)
from page_objects.dashboard_page import StatusElement

@pytest.mark.skip("user should contain full info")
def test_add_text_status(driver, signed_in_user, oxwall_app,status_for_test):

     oxwall_app.dash_page.wait_until_new_status_appeared()
     status_element = oxwall_app.dash_page.status_list[0]
     oxwall_app.dash_page.wait_until_new_status_appeared()


     status_element.add_comment("lilu")
     oxwall_app.dash_page.wait_until_new_status_appeared()
     for i in status_element.get_comment_list:
         print(i.text)
     comment = status_element.get_comment_list[0]
     #print(status_element.get_comment_list.text)
     assert comment.text == "inna"

