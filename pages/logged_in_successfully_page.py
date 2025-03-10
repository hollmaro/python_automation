from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# Class LoggedInSuccessPage inherits from BasePage
# and contains locators and methods for the login page
# representation of https://practicetestautomation.com/logged-in-successfully/

class LoggedInSuccessPage(BasePage):
    search_field = (By.XPATH, "//*[@id='search2']")
    title_text = (By.XPATH, "//h1")
    login_url = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, driver):
        # Initialize the LoginPage instance with a WebDriver object and locators.
        super().__init__(driver)

    def get_title_text(self):
        return self.driver.find_element(*self.title_text).text

    def open_logged_in_success_page(self):
        self.open_page(self.login_url)
        return self
