from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.find_element(By.ID, "name").send_keys("Pranabesh")

driver.find_element(By.ID, "alertbtn").click()

alert = Alert(driver)

print(alert.text)

time.sleep(10)

alert.accept()

driver.quit()