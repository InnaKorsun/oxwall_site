from selenium.webdriver.common.by import By

from page_objects.custom_expected_condition.expected_condition import amount_of_element_located
from page_objects.internal_page import InternalPage
from page_objects.page import InputTextElement


class StatusElement:
    STATUS_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string.ow_small > a")
    STATUS_TEXT = (By.CSS_SELECTOR, ".ow_newsfeed_content")
    STATUS_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")

    def __init__(self, webelement):
        self.webelement = webelement

    @property
    def text(self):
        return self.webelement.find_element(*self.STATUS_TEXT).text

    @property
    def user(self):
        return self.webelement.find_element(*self.STATUS_USER).text

    @property
    def time(self):
        return self.webelement.find_element(*self.STATUS_TIME).text


class DashboardPage(InternalPage):
    STATUS_TEXT_FIELD = (By.NAME, "status")
    SEND_BUTTON = (By.NAME, "save")
    STATUS_BOX = (By.XPATH, "//li[contains(@id, 'action-feed')]")


    def is_this_page(self):
        return self.active_menu.text == "DASHBOARD"

    @property
    def status_text_field(self):
        return InputTextElement(self.find_visible_element(self.STATUS_TEXT_FIELD))

    @property
    def send_button(self):
        return self.find_visible_element(self.SEND_BUTTON)

    @property
    def status_list(self):
        return [StatusElement(el) for el in self.driver.find_elements(*self.STATUS_BOX)]

    def wait_until_new_status_appeared(self):
        old_number = len(self.status_list)
        self.wait.until(amount_of_element_located(self.STATUS_BOX, old_number+1), "No new status detected")