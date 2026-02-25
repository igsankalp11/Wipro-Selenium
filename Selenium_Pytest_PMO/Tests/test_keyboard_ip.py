import time

from execnet.gateway_base import serve
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager


class Test_Keyboard:
    def test_keyboard(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        time.sleep(2)

        actions = ActionChains(driver)
        email = driver.find_element(By.XPATH, "//input[@name='email']")
        seriesofactions = actions.move_to_element(email).key_down(Keys.SHIFT).send_keys("hello").key_up(Keys.SHIFT).key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).key_down(Keys.TAB).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).key_down(Keys.TAB).key_down(Keys.ENTER)


        seriesofactions.perform()
        #password = driver.find_element(By.XPATH, "//input[@id='password']")

        #seriesofactions= actions.move_to_element(password).key_down(Keys.CONTROL).send_keys('v').key_down(Keys.TAB).key_down(Keys.ENTER)
        time.sleep(3)

        driver.close()