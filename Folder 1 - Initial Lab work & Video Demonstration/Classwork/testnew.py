from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

try:
    driver.get("https://www.duckduckgo.com/")

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(
        EC.title_contains("Selenium")
    )

    print("Browser:", driver.capabilities.get("browserName"))
    print("Page title:", driver.title)

    driver.save_screenshot("selenium_firefox_proof.png")
    print("Screenshot saved successfully.")

finally:
    driver.quit()
    print("Test completed successfully.")