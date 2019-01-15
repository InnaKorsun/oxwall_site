from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import Select
import pymysql
from oxwall_site.page_objects.page import InputTextElement, Page


class JoinPage(Page):
    REG_TEXT = (By.XPATH,"//form[@id='joinForm']")
    #USERNAME_FIELD = (By.XPATH,"//input[contains(@id,'input')]")
    #USERNAME_FIELD = (By.CLASS_NAME,'ow_username_validator')
    #USERNAME_FIELD = (By.XPATH,"//input[@class='ow_username_validator']")[2]
    USERNAME_FIELD = (By.XPATH,'//td[contains(@class,"ow_alt1 ow_value")]//input[contains(@class,"ow_username_validator")]')
    #USERNAME_FIELD = (By.XPATH, '//td[contains(@class,"ow_alt1 ow_value")]')
    EMAIL_FIELD = (By.NAME,'email')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')

    REPEAT_PASSWORD_FIELD = (By.NAME, 'repeatPassword')
    #REAL_NAME = (By.XPATH, '//td[contains(@class,"ow_alt1 ow_value")]')[5]
    REAL_NAME = (By.XPATH,'//td[contains(@class,"ow_alt1 ow_value")]/input')
    GENDER_MALE= (By.XPATH,'//li//input[@type = "radio"]')

    GENDER_FEMALE =(By.XPATH, '//input[@type = "radio"]')
    DAY_BIRTHDAY = (By.XPATH,'// select[contains( @ name, "day")]')
    MONTH_BIRTH = (By.XPATH,'// select[contains( @ name, "month")]')

    YEAR_BIRTH = (By.XPATH,'// select[contains( @ name, "year")]')
    JOIN_BUTTON = (By.XPATH,'//input[@name="joinSubmit"]')

    @property
    def username_field(self):

        a =  self.driver.find_elements(*self.USERNAME_FIELD)
        #self.wait.until(visibility_of_element_located(self.USERNAME_FIELD))
        print(a[1].is_displayed())
        return InputTextElement(a[1])

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
        print(a[5].is_displayed())
        return InputTextElement(a[5])

    @property
    def gender_male(self):
        male = self.find_visible_elements(self.GENDER_MALE)[6]
        if not male.is_selected():
            male.click()

    @property
    def gender_female(self):
        female_all =  self.driver.find_elements(*self.GENDER_MALE)
        female = female_all[7]
        if not female.is_selected():
            female.click()

    @property
    def birthday_select(self,day,mon,year):
        select_day = Select(self.find_elements(self.DAY_BIRTHDAY)[1])
        select_day.select_by_value(str(day))
        select_mon = Select(self.find_elements(self.MONTH_BIRTH)[1])
        select_mon.select_by_value(str(mon))
        select = Select(self.find_elements(self.YEAR_BIRTH)[1])
        select.select_by_value(str(year))

    @property
    def join_button(self):
        return self.find_visible_element(self.JOIN_BUTTON)

    def wait_join_page(self):
        self.wait.until(visibility_of_element_located(self.REG_TEXT))

    def fill_in_join_form(self,user_info):
        import time
        time.sleep(3)
        self.wait_join_page()
        print("HERE")
        self.username_field.input(user_info["username"])

        #self.username_field.send_keys(user_info["username"])
        self.email_field.input((user_info["email"]))

        self.password_field.input((user_info["password"]))

        self.repeat_password_field.input((user_info["password"]))
        self.real_name_field.input((user_info["real_name"]))

        if user_info["gender"] == "male":
            self.gender_male
        else:
            self.gender_female
            self.birthday_select(day="1",mon="1",year='1990')
        self.join_button.click()

