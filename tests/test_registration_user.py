from oxwall_site_model import OxwallSite
from value_models.status import Status
import pytest
from data.status_data import status_data

user_info = dict(username="Lola", email="lola_dir@gmail.com", password="12345",
                     real_name="Lola Kim", gender="female") #Birthday="01.01.1990")
def test_join_user(driver,oxwall_app):

    oxwall_app.main_page.sign_in_click()
    oxwall_app.sign_in_page.click_to_join()
    oxwall_app.wait_until_new_status_appeared()

    oxwall_app.join_page.fill_in_join_form(user_info)
    print("ok")

