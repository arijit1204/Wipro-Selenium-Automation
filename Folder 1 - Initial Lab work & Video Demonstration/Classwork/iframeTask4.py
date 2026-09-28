from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.maximize_window()

outerframe = driver.find_element(
    By.XPATH, "//frame[@name='frame-top']"
)

driver.switch_to.frame(outerframe)

innerframe = driver.find_element(
    By.XPATH, "//frame[@name='frame-middle']"
)

driver.switch_to.frame(innerframe)

textbox = driver.find_element(
    By.XPATH, "//body"
)

print("Text inside inner frame:", textbox.text)

time.sleep(2)

driver.switch_to.default_content()

driver.quit()