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

        checkbox_list = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
        count = len(checkbox_list)
        print(count)

        for i in checkbox_list:
            time.sleep(2)
            i.click()

        driver.close()






