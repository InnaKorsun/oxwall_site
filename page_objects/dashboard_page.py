import time


from selenium.webdriver.common.by import By

from page_objects.custom_expected_condition.expected_condition import amount_of_element_located
from page_objects.internal_page import InternalPage
from page_objects.page import InputTextElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class StatusElement():

    STATUS_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string.ow_small > a")
    STATUS_TEXT = (By.CSS_SELECTOR, ".ow_newsfeed_content")
    STATUS_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")
    STATUS_DELETE_ITEM  = (By.XPATH, "//div[contains(@class,'ow_context_action')]")
    NEW_DELETE_BUTTON = (By.XPATH, "//a[contains(@class,'newsfeed_remove_btn owm_red_btn')]")
    ALERT_AGREE_DELETE = (By.TAG_NAME, "alert")

    ADD_COMMENT_ICON = (By.XPATH, "//*[contains(@class,'newsfeed_comment_btn')]")
    COMMENT_BODY = (By.XPATH, "//textarea[@class='comments_fake_autoclick']")
    COMMENT_ITEM = (By.XPATH, '//div[@class ="comments_list_cont"]')
    COMMENT_ITEM_FULL = (By.XPATH, "//li[contains(@id, 'action-feed')][1]/div[1]/div[2]/div[3])")



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

    @property
    def comment_icon(self):
        return self.webelement.find_element(*self.ADD_COMMENT_ICON)

    @property
    def comment_body(self):
        return self.webelement.find_element(*self.COMMENT_BODY)

    @property
    def delete_item(self):
        return self.driver.find_elements(*self.NEWS_DELETE_ITEM)

    @property
    def delete_button(self):
        return self.driver.find_elements(*self.NEW_DELETE_BUTTON)

    @property
    def get_comment_list(self):

        return [CommentToNewsfeed(com) for com in self.webelement.find_elements(*self.COMMENT_ITEM)]

    #@property
    #def get_comment_list(self):
    #    return [CommentToNewsfeed(com) for com in self.webelement.find_element(*self.COMMENT_ITEM_FULL)]

    def add_comment(self,comment):
        self.comment_icon.click()
        self.comment_body.clear()
        self.comment_body.send_keys(comment)
        self.comment_body.send_keys(Keys.ENTER)
        #new_comment = CommentToNewsfeed(*self.COMMENT_ITEM_FULL)
        #print(new_comment.text)
        #return new_comment

    def delete_last_status(self):

        delete_item_cur = self.delete_item[0]
        delete_item_cur.click()

        delete_button_cur = self.delete_button[0]
        delete_button_cur.click()

        time.sleep(1)
        self.driver.switch_to_alert().accept()

    def click_to_elem(self):
        self.click()

class CommentToNewsfeed:

    COMMENT_TEXT = (By.XPATH, "//div[@class ='ow_comments_content ow_smallmargin']")

    def __init__(self, webelement):
        self.webelement = webelement


    @property
    def text(self):
        return self.webelement.find_element(*self.COMMENT_TEXT).text



class DashboardPage(InternalPage):

    STATUS_TEXT_FIELD = (By.NAME, "status")
    SEND_BUTTON = (By.NAME, "save")
    STATUS_BOX = (By.XPATH, "//li[contains(@id, 'action-feed')]")

    COMMENT_ITEM = (By.XPATH, '//div[@class ="comments_list_cont"]')



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
        #return [el for el in self.driver.find_elements(*self.STATUS_BOX)]

    @property
    def get_comment_list(self):
        return [el for el in self.driver.find_elements(*self.COMMENT_ITEM)]

    #def wait_until_new_status_appeared(self):
    #    old_number = len(self.status_list)
    #    self.wait.until(amount_of_element_located(self.STATUS_BOX, old_number+1), "No new status detected")

    def wait_until_new_status_appeared(self):
        time.sleep(3)

