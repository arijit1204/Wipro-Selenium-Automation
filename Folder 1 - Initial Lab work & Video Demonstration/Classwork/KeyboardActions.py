from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.maximize_window()

time.sleep(3)

# Locate left textbox using XPath
left_textbox = driver.find_element(
    By.XPATH,
    "(//textarea)[1]"
)

# Move to the element first
actions = ActionChains(driver)

actions.move_to_element(left_textbox)
actions.click()
actions.send_keys("Welcome to Selennium")
actions.perform()

time.sleep(10)