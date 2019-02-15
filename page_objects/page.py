from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable, \
    visibility_of_any_elements_located


class InputTextElement:
    def __init__(self, webelement):
        self.element = webelement

    def input(self, text):
        """Sets the text to the value supplied"""
        self.element.clear()
        self.element.send_keys(text)

    @property
    def placeholder(self):
        """Gets the text of the specified object"""
        return self.element.get_attribute("placeholder")

    @property
    def text(self):
        """Gets the text of the specified object"""
        return self.element.get_attribute("value")


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action_chain = ActionChains(driver)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def find_visible_element(self, locator):
        return self.wait.until(visibility_of_element_located(locator), "No visible element with {}".format(locator))


    def find_clickable_element(self, locator):
        return self.wait.until(element_to_be_clickable(locator))

    def find_any_visibility_elements(self, locator):
         return self.wait.until(visibility_of_any_elements_located(*locator))


    @property
    def current_url(self):
        return self.driver.current_url

    def refresh_page(self):
        self.driver.refresh()