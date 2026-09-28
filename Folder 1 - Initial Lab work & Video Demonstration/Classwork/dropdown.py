from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import Select

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

# Locate the dropdown
dropdown = Select(
    driver.find_element(By.ID, "dropdown-class-example")
)

# Select Option1
dropdown.select_by_visible_text("Option1")

#Other options
dropdown.select_by_value("option1")
dropdown.select_by_index(1)


time.sleep(8)

driver.quit()