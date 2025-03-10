from selenium.webdriver.common.by import By


from pages.logged_in_successfully_page import LoggedInSuccessPage
from pages.base_page import BasePage


# Class LoginPage inherits from BasePage
# and contains locators and methods for the login page
# representation of https://practicetestautomation.com/practice-test-login/

class LoginPage(BasePage):
    def __init__(self, driver):
        # Викликаємо конструктор базового класу BasePage через super() і передаємо йому драйвер
        # (об'єкт WebDriver який потім буде використовуватися в методах класу)
        super().__init__(driver)

    # локатори елементів сторінки логіну
    search_field = (By.XPATH, "//*[@id='search2']")
    user_name_field = (By.ID, "username")
    password_field = (By.ID, "password")
    submit_button = (By.ID, "submit")
    login_url = "https://practicetestautomation.com/practice-test-login/"

    def enterUserCred(self, username, password):
        self.enter_text(self.user_name_field, username)
        self.enter_text(self.password_field, password)
        return self

    def open_login_page(self):
        self.open_page(self.login_url)
        return self

    def clickOnSubmit(self):
        self.click_on_web_element(self.submit_button)
        return LoggedInSuccessPage(self.driver)
