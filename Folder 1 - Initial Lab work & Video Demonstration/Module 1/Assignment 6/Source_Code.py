from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

time.sleep(5)

driver.switch_to.frame("mce_0_ifr")

text = driver.find_element(By.ID, "tinymce")
print(text.text)

driver.switch_to.default_content()

driver.get("https://the-internet.herokuapp.com/windows")

time.sleep(5)

main_window = driver.current_window_handle

driver.find_element(By.LINK_TEXT, "Click Here").click()

time.sleep(5)

windows = driver.window_handles

for window in windows:
    if window != main_window:
        driver.switch_to.window(window)
        print(driver.title)
        driver.close()
        break

driver.switch_to.window(main_window)

print(driver.title)

driver.quit()