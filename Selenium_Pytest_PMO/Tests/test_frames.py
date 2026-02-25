import time

from execnet.gateway_base import serve
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

class Test_Frames:
    def test_frames(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.get("https://jqueryui.com/datepicker/")
        driver.maximize_window()
        time.sleep(2)
        driver.implicitly_wait(10)
        # frame = driver.find_element(By. XPATH, "//iframe[@class='demo-frame' ]")
        driver.switch_to.frame(0)

        datepicker = driver.find_element(By.XPATH, "//input[@id='datepicker']")
        datepicker.click()
        driver.close()