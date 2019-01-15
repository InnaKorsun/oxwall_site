from oxwall_site.page_objects.internal_page import InternalPage
from oxwall_site.page_objects.signing_in_page import SignInPage


class MainPage(InternalPage):
    pass

    # TODO Add all elements and actions that you have in Main Page

    def sign_in_click(self):
        self.sign_in_menu.click()
        # Maybe some explicit wait
        # return SignInPage(self.driver)


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/oxwall")
    main_page = MainPage(driver)
    main_page.sign_in_menu.click()