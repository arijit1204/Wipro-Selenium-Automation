from selenium import webdriver
from selenium.webdriver.common.by import By
import time

test_data = [
    ("standard_user", "secret_sauce", "success"),
    ("wrong_user", "secret_sauce", "error"),
    ("standard_user", "wrong_password", "error"),
    ("wrong_user", "wrong_password", "error")
]

for username, password, expected in test_data:

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    time.sleep(5)

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    time.sleep(5)

    if expected == "success":
        assert "/inventory.html" in driver.current_url
    else:
        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert error.is_displayed()

    driver.quit()