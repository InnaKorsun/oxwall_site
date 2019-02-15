
from pytest_bdd import given, when, then


@given("initial amount of status in Oxwall database")
def initial_amout_status(db):
    return db.count_status()

@given("I as a logged user")
def signed_in_user(driver, user_one, oxwall_app):
    oxwall_app.login_as(user_one)
    yield user_one
    oxwall_app.logout_as(user_one)

@when("I add a status with <text> in Dashboard page")
def add_status(oxwall_app,text,db):
    old_count = db.count_status()
    oxwall_app.dash_page.status_text_field.input(text)
    oxwall_app.dash_page.send_button.click()
    return old_count


@then("a new status block appears before old list of status")
def wait_new_news(oxwall_app):
    oxwall_app.dash_page.wait_until_new_status_appeared()
    #assert db.count_status() == int(add_status()) + 1

@then('this status block has this <text> and author as this user and time "within 1 minute"')
def verify_status_block(oxwall_app,text,signed_in_user):
    new_status = oxwall_app.dash_page.status_list[0]
    assert text == new_status.text, f"Status text '{text}' is displayed incorrect"
    assert signed_in_user.real_name == new_status.user
    assert "within 1 minute" == new_status.time