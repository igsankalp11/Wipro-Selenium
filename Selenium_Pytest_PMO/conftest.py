# create a fixture for invoke chrome browser


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope = "function")
def driver(request):
    service = Service(ChromeDriverManager().install())
    #driver instance is created to use globally in test script
    driver = webdriver.Chrome(service = service)
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/")

    request.cls.driver = driver
    yield
    driver.quit()