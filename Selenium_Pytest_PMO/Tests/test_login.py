# check the title of the web page
import time

import pytest

from Selenium_Pytest_PMO.Pages.Login_page import LoginPage


@pytest.mark.usefixtures("driver")
class TestLogin:


    def test_valid_login(self, driver):
        #time.sleep(3s)
        lp = LoginPage(driver)
        lp.login("Admin","admin123")
        assert "OrangeHRM" in driver.title

