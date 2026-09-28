from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/autocomplete/")

time.sleep(5)

driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

driver.find_element(By.ID, "tags").send_keys("Ja")

time.sleep(5)

suggestions = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item")

for option in suggestions:
    if option.text == "Java":
        option.click()
        break

driver.switch_to.default_content()

driver.get("https://the-internet.herokuapp.com/checkboxes")

time.sleep(5)

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

checkboxes[0].click()

assert checkboxes[0].is_selected()

driver.quit()