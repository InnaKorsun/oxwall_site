import json
import pytest
import os.path
from selenium import webdriver

from .value_models.user import User
from db.db_connector import DBConnector
from value_models.status import Status
from .oxwall_site_model import OxwallSite

@pytest.fixture(scope='session')
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

with open(os.path.join(PROJECT_DIR, "config.json")) as f:
    config = json.load(f)


@pytest.fixture(scope="session")
def db():
    db = DBConnector(config["db"])
    yield db
    db.close()


with open(os.path.join(PROJECT_DIR, "data", "user_data.json")) as f:
    user_data = json.load(f)


@pytest.fixture(params=user_data, ids=[str(user) for user in user_data], scope='session')
def user(request, db):
    user = User(**request.param)
    db.create_user(user)
    yield user
    db.delete_user(user)


@pytest.fixture(scope="session")
def admin():
    params = config["web"]["admin"]
    return User(**params, is_admin=True, real_name=params["username"].title())


@pytest.fixture(scope="session")
def oxwall_app(driver):
    app = OxwallSite(driver)
    return app


@pytest.fixture(scope="session")
def signed_in_user(driver, user, oxwall_app):
    oxwall_app.login_as(user)
    yield user
    oxwall_app.logout_as(user)


@pytest.fixture(scope="session")
def signed_as_admin(driver, admin, oxwall_app):
    oxwall_app.login_as(admin)
    yield admin
    oxwall_app.logout_as(admin)


@pytest.fixture(scope="session")
def status_for_test(driver, signed_in_user, oxwall_app):
    status = Status(text="Status for test", user=signed_in_user)

    oxwall_app.dash_page.status_text_field.input(status.text)
    oxwall_app.dash_page.send_button.click()
    oxwall_app.dash_page.wait_until_new_status_appeared()


@pytest.fixture()
def logout(driver, oxwall_app):
    yield
    # app = OxwallSite(driver)
    oxwall_app.dash_page.sign_out()
