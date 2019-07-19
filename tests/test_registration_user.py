from oxwall_site_model import OxwallSite
from value_models.status import Status
import pytest
from data.status_data import status_data
from  mimesis import Person
person = Person("en")

user_info = dict(username=person.last_name(), email=person.email(),password=person.password(),
                     real_name=person.full_name(), gender='men', birthday = ("1","3","1990"))
print(user_info)

#user_info = dict(username="iern_vol", email="irena_director@gmail.com", password="12345",
 #                    real_name="Irena Solo", gender="female", birthday = ("1","3","1990"))
#@pytest.mark.skip("doesnt work")

def test_join_user(driver,oxwall_app):

    oxwall_app.main_page.sign_in_click()
    oxwall_app.sign_in_page.click_to_join()
    oxwall_app.wait_until_new_status_appeared()

    oxwall_app.join_page.fill_in_join_form(user_info)
    actual_text = oxwall_app.dash_page.text_status_new_user
    print (actual_text)
    print( user_info["real_name"]+" joined our site!")
    assert user_info["real_name"]+" joined our site!" == actual_text




