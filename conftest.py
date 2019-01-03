import json
import pytest
import os.path
from selenium import webdriver

from oxwall_site_model import OxwallSite
from value_models.user import User


@pytest.fixture(scope="session")
def driver():
    # Open browser driver settings
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    # driver.get('http://127.0.0.1/oxwall/')
    yield driver
    # Close browser
    driver.quit()


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(PROJECT_DIR, "data", "user_data.json")) as f:
    user_data = json.load(f)


@pytest.fixture(params=user_data, ids=[str(user) for user in user_data],scope="session")
def user(request):
    return User(**request.param)


@pytest.fixture(scope="session")
def signed_in_user(driver, user):
    app = OxwallSite(driver)
    app.login_as(user)
    yield user
    app.logout_as(user)


@pytest.fixture()
def logout(driver):
    yield
    app = OxwallSite(driver)
    app.dash_page.sign_out()