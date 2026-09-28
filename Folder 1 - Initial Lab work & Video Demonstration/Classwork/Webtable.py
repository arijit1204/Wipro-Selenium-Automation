from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

table = driver.find_element(By.ID, "productTable")
driver.execute_script("arguments[0].scrollIntoView();", table)

time.sleep(2)

target_ids = ["1", "3", "5"]

rows = driver.find_elements(
    By.XPATH,
    "//table[@id='productTable']/tbody/tr"
)

for row in rows:
    row_id = row.find_element(By.XPATH, "./td[1]").text

    if row_id in target_ids:
        checkbox = row.find_element(By.XPATH, "./td[4]/input")
        checkbox.click()
        print(f"Selected ID: {row_id}")

time.sleep(3)

driver.quit()