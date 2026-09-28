from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(2) #The webpage will stay for 2 ms
language_link = driver.find_element(By.LINK_TEXT, "About") #It will get the about link
language_link.click() #The about page will be opened 

driver.quit()