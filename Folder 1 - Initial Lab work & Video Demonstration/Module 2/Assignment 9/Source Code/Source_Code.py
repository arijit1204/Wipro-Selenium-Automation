import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("reports", exist_ok=True)
        driver.save_screenshot("reports/failed_test.png")

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)

def test_saucedemo_login(driver):
    driver.get("https://www.saucedemo.com/")

    time.sleep(5)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(5)

    assert "/inventory.html" in driver.current_url