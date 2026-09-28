from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.maximize_window()

assert "/inventory.html" in driver.current_url

time.sleep(5)

driver.quit()