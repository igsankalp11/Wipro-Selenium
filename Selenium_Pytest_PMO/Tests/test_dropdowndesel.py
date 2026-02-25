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
        driver.get("https://trytestingthis.netlify.app/")

        time.sleep(2)

# Multi select element
        multi = driver.find_element(By.ID, "owc")

# Select class
        select = Select(multi)

#  Option 1
        select.select_by_visible_text("Option 1")

#  Option 2
        select.select_by_visible_text("Option 2")

        time.sleep(2)

        print("Selected Options:")
        for option in select.all_selected_options:
            print(option.text)

        #  Option 1 deselect
        select.deselect_by_visible_text("Option 1")
        print("All options deselected")

        time.sleep(2)

        driver.close()




