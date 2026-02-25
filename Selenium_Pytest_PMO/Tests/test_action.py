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
        driver.maximize_window()
        driver.get("https://www.amazon.in/")
        time.sleep(2)

        actions = ActionChains(driver)
        bestsellers = driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
        # double click using actions class
        actions.double_click(bestsellers).perform()  # double click
        time.sleep(2)
        driver.back()
        time.sleep(2)

        mobiles = driver.find_element(By.CSS_SELECTOR, ".nav-a[href='/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles']")
        actions.context_click(mobiles).perform()  # right click
        time.sleep(2)

        driver.back()
        time.sleep(2)

        # move to element
        primes = driver.find_element(By.XPATH, "//span[normalize-space()='Prime']")
        actions.move_to_element(primes).perform()

        # click and hold
        fresh = driver.find_element(By.XPATH, "//span[normalize-space()='Fresh']")
        actions.click_and_hold(fresh).perform()



        driver.close()