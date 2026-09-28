from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

file_path = os.path.abspath("sample.txt")

with open(file_path, "w") as file:
    file.write("Hello Selenium")

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.maximize_window()

time.sleep(3)

upload = driver.find_element(By.CSS_SELECTOR, "input[type='file']")

upload.send_keys(file_path)

time.sleep(5)

print("File uploaded successfully")

driver.quit()