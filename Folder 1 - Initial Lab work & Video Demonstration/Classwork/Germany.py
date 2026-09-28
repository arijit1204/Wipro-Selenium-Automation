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

# Suggestion Class Example
suggestion_box = driver.find_element(By.ID, "autocomplete")
suggestion_box.send_keys("Germany")

# Select Germany from the suggestion
# germany = driver.find_element(
#     By.XPATH, "//div[contains(@class,'ui-menu-item') and contains(.,'Germany')]"
# )

germany.click()

driver.find_element(By.ID, "autocomplete").send_keys("Germany")
options = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item")
for option in options:
    if option.text == "Germany":
        option.click()
        break  

time.sleep(10)

driver.quit()