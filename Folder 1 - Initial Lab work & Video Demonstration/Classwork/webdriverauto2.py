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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

# radio2 = driver.find_element(By.XPATH, "(//input[@type='radio'])[2]")
# radio2.click()
radio2 = driver.find_element(By.XPATH, "//input[@value='radio2']")
radio2.click()

time.sleep(8)

driver.quit()