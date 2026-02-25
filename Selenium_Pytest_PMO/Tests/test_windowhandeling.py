import time

from execnet.gateway_base import serve
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

class Test_Winhan:
    def test_winhan(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/windows")
        driver.maximize_window()

        time.sleep(2)
        driver.implicitly_wait(10)
        clickhere = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
        clickhere.click()
        # fetch the window handles of both tabs
        windows = driver.window_handles
        print(windows)
        # move the control to the child window
        driver.switch_to.window(windows[1])
        time.sleep(2)

        text = driver.find_element(By.XPATH, "//h3[contains(text(),'New Window')]")
        print(text)
        driver.close()
        # get back to parent window
        driver.switch_to.window(windows[0])
        clickhere.is_displayed()

        driver.close()