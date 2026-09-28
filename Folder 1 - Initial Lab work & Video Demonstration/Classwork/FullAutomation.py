from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time


browsername = "chrome"

if browsername.lower() == "chrome":
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

elif browsername.lower() == "firefox":
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

else:
    raise Exception("Invalid browser name. Please choose chrome or firefox")


driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()


name = driver.find_element(By.XPATH, "//input[@id='name']")
name.send_keys("Pranabesh Basu")


address = driver.find_element(By.XPATH, "//textarea[@id='textarea']")
address.send_keys("Kolkata, West Bengal")


email = driver.find_element(By.XPATH, "//input[@id='email']")
email.send_keys("test@gmail.com")


phone = driver.find_element(By.XPATH, "//input[@id='phone']")
phone.send_keys("98765XXXXX")



male = driver.find_element(By.XPATH, "//input[@id='male']")
male.click()



monday = driver.find_element(By.XPATH, "//input[@id='monday']")
monday.click()

tuesday = driver.find_element(By.XPATH, "//input[@id='tuesday']")
tuesday.click()

wednesday = driver.find_element(By.XPATH, "//input[@id='wednesday']")
wednesday.click()

thursday = driver.find_element(By.XPATH, "//input[@id='thursday']")
thursday.click()

friday = driver.find_element(By.XPATH, "//input[@id='friday']")
friday.click()


dropdown = Select(
    driver.find_element(By.XPATH, "//select[@id='country']")
)

dropdown.select_by_visible_text("India")


color_dropdown = Select(
    driver.find_element(By.XPATH, "//select[@id='colors']")
)

color_dropdown.select_by_visible_text("Red")



date = driver.find_element(By.XPATH, "//input[@id='datepicker']")
date.send_keys("08/31/2026")

submit = driver.find_element(By.XPATH, "//button[text()='Submit']")
submit.click()

time.sleep(10)

driver.quit()