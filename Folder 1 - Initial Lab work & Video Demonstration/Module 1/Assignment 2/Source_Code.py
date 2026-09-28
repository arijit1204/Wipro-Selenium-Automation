from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

driver.find_element(By.XPATH, "//button[text()='Start']").click()

text_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "finish"))
)

print(text_element.text)

driver.quit()