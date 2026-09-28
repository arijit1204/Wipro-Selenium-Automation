from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

parent_window = driver.current_window_handle
print(parent_window)

driver.find_element(By.XPATH, "//button[contains(text(),'New Tab')]").click()

time.sleep(2)

windows = driver.window_handles
print(windows)

driver.switch_to.window(windows[1])

time.sleep(3)

driver.close()

driver.switch_to.window(parent_window)

driver.find_element(By.ID, "name").send_keys("Pranabesh")

time.sleep(3)

driver.quit()