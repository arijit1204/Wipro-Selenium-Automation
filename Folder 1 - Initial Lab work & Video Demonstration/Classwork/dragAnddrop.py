from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(2)

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

actions = ActionChains(driver)

actions.click_and_hold(source)
actions.move_to_element(target)
actions.release()
# actions.drag_and_drop(source, target)
actions.perform()

time.sleep(5)

driver.quit()