import time

import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest


@pytest.mark.usefixtures("driver_init")
# TestLogin клас, який успадковує BaseTest клас для виведення назви тесту перед його виконанням
# Тестовий клас має починатися зі слова Test для того, щоб pytest визначив його як тест
class TestLogin(BaseTest):
    # Позитивний тест на вхід в систему
    # Тестовий метод має починається зі слова test_ для того, щоб pytest визначив його як тест
    def test_login_positive(self, driver_init):
        login_p = LoginPage(driver_init)
        title = (login_p
                 .open_login_page()
                 .enterUserCred('student', 'Password123')
                 .clickOnSubmit()
                 .get_title_text())
        time.sleep(5)
        assert "Logged In Successfully" in title
