import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_MultiSelectRadio:
        def test_multiradio(self):
            try:
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                driver.maximize_window()

                driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

                Add_to_cart = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]")
                Add_to_cart.click()
                time.sleep(3)

                Add_to_cart = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]")
                Add_to_cart.click()
                time.sleep(4)

                Go_to_cart = driver.find_element(By.XPATH,"//img[@alt='Cart']")
                Go_to_cart.click()
                time.sleep(4)

                checkout = driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']")
                checkout.click()
                time.sleep(4)
                PlaceOrder = driver.find_element(By.XPATH,"//button[normalize-space()='Place Order']")
                PlaceOrder.click()

                driver.close()

            except Exception as e:
                print(f"Error Occured {e}")

            finally:
                print("Successfull")

