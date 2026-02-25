import time

from execnet.gateway_base import serve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

class Test_Dropdown:
    def test_dropdown(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        time.sleep(2)
        # switch the control to alert
        simplealt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
        simplealt.click()
        time.sleep(2)
        alt = driver.switch_to.alert
        alt.accept()  # click on accept button
        time.sleep(2)

        # confirmation alerts
        # switch the control to alert
        confalt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
        confalt.click()
        time.sleep(2)
        alt = driver.switch_to.alert
        alt.dismiss()  # click on cancel button
        time.sleep(2)

        # prompt alerts
        promptalt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt' ]")
        promptalt.click()
        time.sleep(2)
        alt = driver.switch_to.alert
        alerttext = alt.text
        print(alerttext)
        alt.send_keys("test hello")
        time.sleep(1)
        alt.accept()
        time.sleep(2)
        driver.close()

