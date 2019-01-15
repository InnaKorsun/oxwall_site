from selenium.webdriver.support.expected_conditions import invisibility_of_element_located

from oxwall_site.page_objects.dashboard_page import DashboardPage
from oxwall_site.page_objects.page import Page, InputTextElement
from oxwall_site.locators.locator import SignInLocators


class SignInPage(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.username_field = self.find_visible_element(locator.LOGIN_FIELD)
    #  Not good decision, because we can get staleness elements over time

    @property
    def username_field(self):
        return InputTextElement(self.find_visible_element(SignInLocators.LOGIN_FIELD))

    @property
    def password_field(self):
        return InputTextElement(self.find_visible_element(SignInLocators.PASS_FIELD))

    @property
    def sign_in_button(self):
        return self.find_visible_element(SignInLocators.SIGN_IN_BUTTON)

    def is_this_page(self):
        return self.is_element_present(SignInLocators.LOGIN_WINDOW_BOX)

    def click_to_join(self):
        self.find_visible_element(SignInLocators.JOIN_LINK).click()

    def submit_form(self):
        self.sign_in_button.click()
        self.wait.until(invisibility_of_element_located(SignInLocators.LOGIN_BACKGROUND), "DashPage doesn't appear")
        # return DashboardPage(self.driver)

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/oxwall")
    from page_objects.main_page import MainPage
    main_page = MainPage(driver)
    main_page.sign_in_menu.click()

    sign_in_page = SignInPage(driver)
    # 1st type of using:
    sign_in_page.username_field.clear()
    sign_in_page.username_field.send_keys("something")
    sign_in_page.password_field.clear()
    sign_in_page.password_field.send_keys("some_pass")
    sign_in_page.sign_in_button.click()
    # 2nd type of using:
    sign_in_page.input_username("something")
    sign_in_page.input_password("some_pass")
    sign_in_page.submit_form()