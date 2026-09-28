from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browsername = "chrome"

if browsername.lower() == "chrome":
    driver = webdriver.Chrome(
        service = ChromeService(ChromeDriverManager().install())
    )
elif browsername.lower() == "firefox":
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
else:
    raise Exception("Invalid browser name. Please choose chrome or firefox")

driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()
# Name
name = driver.find_element(By.XPATH, "//input[@id='name']")
name.send_keys("Pranabesh")

# Address
address = driver.find_element(By.XPATH, "//textarea[@id='textarea']")
address.send_keys("Kolkata, West Bengal")

# Email
email = driver.find_element(By.XPATH, "//input[@id='email']")
email.send_keys("test@gmail.com")

time.sleep(8)

driver.quit()