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

                driver.get("https://www.saucedemo.com/")
                name = driver.find_element(By.NAME,"user-name")
                name.send_keys("standard_user")

                password = driver.find_element(By.NAME,"password")
                password.send_keys("secret_sauce")

                login_button = driver.find_element(By.XPATH,"//input[@id='login-button']")
                login_button.click()
                time.sleep(3)

                Add_to_cart = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
                Add_to_cart.click()
                time.sleep(4)

                Go_to_cart = driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
                Go_to_cart.click()
                time.sleep(4)

                checkout = driver.find_element(By.XPATH,"//button[@id='checkout']")
                checkout.click()

                Firstname = driver.find_element(By.XPATH,"//input[@id='first-name']")
                Firstname.send_keys("Nishchal")
                time.sleep(4)

                Lastname = driver.find_element(By.XPATH,"//input[@id='last-name']")
                Lastname.send_keys("Umapathi")
                time.sleep(4)

                ZipCode = driver.find_element(By.XPATH,"//input[@id='postal-code']")
                ZipCode.send_keys(546546)
                time.sleep(4)

                Continue = driver.find_element(By.XPATH, "//input[@id='continue']")
                Continue.click()
                time.sleep(3)

                Finish = driver.find_element(By.XPATH, "//button[@id='finish']")
                Finish.click()
                time.sleep(3)

                driver.close()

            except Exception as e:
                print(f"Error Occured {e}")

            finally:
                print("Successfull")