from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    visibility_of_any_elements_located
from selenium.webdriver.support.ui import Select
import pymysql
from page_objects.page import InputTextElement, Page


class JoinPage(Page):
    REG_TEXT = (By.XPATH,"//form[@id='joinForm']")

    USERNAME_FIELD = (By.XPATH,'//input[@class="ow_username_validator"]')

    EMAIL_FIELD = (By.NAME,'email')

    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')

    REPEAT_PASSWORD_FIELD = (By.NAME, 'repeatPassword')

    REAL_NAME = (By.XPATH,'//td[contains(@class,"ow_alt1 ow_value")]/input')

    GENDER_MALE= (By.XPATH,'//input[contains(@type,"radio") and contains(@value,"1")]')
    GENDER_FEMALE =(By.XPATH, '//input[contains(@type,"radio") and contains(@value,"2")]')

    DAY_BIRTHDAY = (By.XPATH,'// select[contains( @ name, "day")]')
    MONTH_BIRTH = (By.XPATH,'// select[contains( @ name, "month")]')
    YEAR_BIRTH = (By.XPATH,'// select[contains( @ name, "year")]')

    JOIN_BUTTON = (By.XPATH,'//input[@name="joinSubmit"]')

    @property
    def username_field(self):
        a =  self.driver.find_elements(*self.USERNAME_FIELD)
        for i in a:
            if i.is_displayed():
                return InputTextElement(i)


    @property
    def email_field(self):
        return InputTextElement(self.find_visible_element(self.EMAIL_FIELD))

    @property
    def password_field(self):
        a = self.driver.find_elements(*self.PASSWORD_FIELD)
        return InputTextElement(a[1])

    @property
    def repeat_password_field(self):
        return InputTextElement(self.find_visible_element(self.REPEAT_PASSWORD_FIELD))

    @property
    def real_name_field(self):
        a = self.driver.find_elements(*self.REAL_NAME)
        #for i in a:
        #    if i.is_displayed():
        #        return InputTextElement(i)
        return InputTextElement(a[5])


    @property
    def gender_male(self):
        male = self.driver.find_elements(*self.GENDER_MALE)
        for i in male:
            if i.is_displayed():
                i.click()



    @property
    def gender_female(self):
        female = self.driver.find_elements(*self.GENDER_FEMALE)
        for i in female:
            if i.is_displayed():
                i.click()

    @property
    def birthday_day(self):
        select_day = self.driver.find_elements(*self.DAY_BIRTHDAY)
        for i in select_day:
            if i.is_displayed():
                print("here")
                return Select(i)

    @property
    def birthday_month(self):
        select_day = self.driver.find_elements(*self.MONTH_BIRTH)
        for i in select_day:
            if i.is_displayed():
                print("here")
                return Select(i)

    @property
    def birthday_year(self):
        select_day = self.driver.find_elements(*self.YEAR_BIRTH)
        for i in select_day:
            if i.is_displayed():
                print("here")
                return Select(i)

    @property
    def join_button(self):
        return self.find_visible_element(self.JOIN_BUTTON)

    def wait_join_page(self):
        self.wait.until(visibility_of_element_located(self.REG_TEXT))

    def fill_in_join_form(self,user_info):
        import time
        time.sleep(3)
        self.wait_join_page()
        self.username_field.input(user_info["username"])

        self.email_field.input((user_info["email"]))

        self.password_field.input((user_info["password"]))

        self.repeat_password_field.input((user_info["password"]))

        self.real_name_field.input((user_info["real_name"]))

        if user_info["gender"] == "male":
            self.gender_male
        else:
            self.gender_female

        self.birthday_day.select_by_value(user_info["birthday"][0])
        self.birthday_month.select_by_value(user_info["birthday"][1])
        self.birthday_year.select_by_value(user_info["birthday"][2])

        import time
        time.sleep(5)
        self.join_button.click()

