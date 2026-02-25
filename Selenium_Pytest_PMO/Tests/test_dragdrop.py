import time

from execnet.gateway_base import serve
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager


class Test_Action:
    def test_action(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        driver.maximize_window()
        time.sleep(2)

        actions = ActionChains(driver)
        source = driver.find_element(By.XPATH, "//div[@id='column-a']")
        dest = driver.find_element(By.XPATH, "//div[@id='column-b']")

        actions.drag_and_drop(source, dest)
        time.sleep(4)
        driver.close()