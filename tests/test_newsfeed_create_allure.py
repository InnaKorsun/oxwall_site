from oxwall_site_model import OxwallSite
from selenium.webdriver.remote.webelement import WebElement
from value_models.status import Status
import pytest
from data.status_data import status_data
import allure

#pytest.mark.skip("doent work teardown")
@pytest.mark.parametrize("status_text",status_data)
@allure.story("Add NEWS")
@allure.feature("CRUD")
def test_add_text_status(driver, signed_as_admin , oxwall_app, status_text,db):

    status = Status(text=status_text, user=signed_as_admin)
    with allure.step("Assert to go main page"):
        assert oxwall_app.dash_page.status_text_field.placeholder == "What’s happening?"

    oxwall_app.dash_page.status_text_field.input(status.text)
    oxwall_app.dash_page.send_button.click()
    oxwall_app.dash_page.wait_until_new_status_appeared()
    new_status = oxwall_app.dash_page.status_list[0]

    with allure.step("Assert new status"):
        assert new_status.text == status.text
        assert new_status.time == "within 1 minute"
    status_from_db = db.get_last_text_status()

    assert status.text == status_from_db.text
    db.delete_status_by_id(status_from_db.id)

