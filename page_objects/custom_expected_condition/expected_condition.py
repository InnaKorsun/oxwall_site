from selenium.webdriver.support.expected_conditions import element_to_be_clickable
class amount_of_element_located:

    def __init__(self, locator, number):
        self.locator = locator
        self.number =  number

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        if len(elements) == self.number:
            return elements
        else:
            return False

