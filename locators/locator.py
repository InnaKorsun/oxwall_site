from selenium.webdriver.common.by import By


class InternalPageLocators:
    ACTIVE_MENU = (By.XPATH, "//div[contains(@class, 'ow_menu_wrap')]//li[contains(@class, 'active')]")
    DASHBOARD_MENU = (By.LINK_TEXT, "DASHBOARD")
    MAIN_MENU = (By.LINK_TEXT, "MAIN")
    PHOTO_MENU = ()  # TODO
    # TODO Add other menu locators
    SIGN_IN_MENU = (By.XPATH, '//*[contains(@id,"console_item")]/span[1]')
    USER_MENU = (By.XPATH, "//div[contains(@class,'ow_console_dropdown_hover')]")
    SIGN_OUT_LINK = (By.XPATH, './/a[contains(@href,"sign-out")]')


class SignInLocators:
    LOGIN_FIELD = (By.NAME, 'identity')
    PASS_FIELD = (By.NAME, 'password')
    SIGN_IN_BUTTON = (By.XPATH, "//div[@class='ow_right']")
    LOGIN_BACKGROUND = (By.ID, "floatbox_overlay")
    LOGIN_WINDOW_BOX = (By.CLASS_NAME, "floatbox_container")
    JOIN_LINK = (By.XPATH, "//div[@class='ow_sign_up']/p[2]/a")

