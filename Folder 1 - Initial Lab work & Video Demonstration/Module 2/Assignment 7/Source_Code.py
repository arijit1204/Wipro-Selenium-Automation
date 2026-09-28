from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage:

    username = (By.ID, "user-name")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//input[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self):
        return self.driver.current_url


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

time.sleep(5)

login_page = LoginPage(driver)
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login()

time.sleep(5)

inventory_page = InventoryPage(driver)

assert "/inventory.html" in inventory_page.get_url()

driver.quit()