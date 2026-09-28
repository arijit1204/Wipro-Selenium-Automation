from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(3)

min_slider = driver.find_element(By.XPATH, "//div[@id='HTML7']//span[1]")
max_slider = driver.find_element(By.XPATH, "//div[@id='HTML7']//span[2]")

actions = ActionChains(driver)

actions.click_and_hold(min_slider).move_by_offset(30, 0).release().perform()

time.sleep(2)

actions.click_and_hold(max_slider).move_by_offset(-20, 0).release().perform()

time.sleep(5)

driver.quit()