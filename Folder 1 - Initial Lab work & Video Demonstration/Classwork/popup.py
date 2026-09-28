from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.find_element(By.ID, "name").send_keys("Pranabesh")

alert_button = driver.find_element(By.ID, "alertbtn")
alert_button.click()

alert = driver.switch_to.alert

print(alert.text)

time.sleep(10)

alert.accept()

driver.quit()