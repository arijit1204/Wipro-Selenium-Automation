from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/tables")

time.sleep(5)

rows = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")

for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")

    for column in columns:
        print(column.text, end=" | ")

    print()

for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")

    if columns[1].text == "Frank":
        status = columns[4].text
        print("Status:", status)
        break

driver.quit()