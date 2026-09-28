from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(3)

driver.save_screenshot("testautomationpractice.png")

print("Screenshot saved successfully.")

driver.quit()