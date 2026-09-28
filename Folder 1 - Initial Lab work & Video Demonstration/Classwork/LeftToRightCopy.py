from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.maximize_window()

time.sleep(2)

left_textbox = driver.find_element(
    By.XPATH, "(//textarea)[1]"
)

right_textbox = driver.find_element(
    By.XPATH, "(//textarea)[2]"
)

actions = ActionChains(driver)


actions.click(left_textbox).send_keys("Welcome to Selennium").perform()

actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

actions.click(right_textbox).perform()

actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

pasted_text = right_textbox.get_attribute("value")

print("Text pasted in the right textbox:", pasted_text)

time.sleep(5)

driver.quit()