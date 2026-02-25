import time

from execnet.gateway_base import serve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class Test_Radio:
    def test_radio(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        time.sleep(2)

        driver.find_elements(By.XPATH, "//input[@value='radio2']").click()

        driver.close()





