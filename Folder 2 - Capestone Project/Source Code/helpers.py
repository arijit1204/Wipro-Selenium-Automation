# helpers.py
# The reusable pieces. main.py decides WHAT happens in the purchase flow,
# this file holds HOW each small job is done.

import json
import os
from datetime import datetime

from openpyxl import load_workbook
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import settings

# These two lists fill up while the flow runs and feed the report at the end.
results = []                # one (step, status, note) tuple per step
screenshots_taken = []      # file names of every screenshot saved


# ---------------------------------------------------------------------
# TASK 8 - read test data from JSON or Excel
# ---------------------------------------------------------------------
def read_test_data():
    if settings.DATA_SOURCE == "json":
        with open(settings.JSON_FILE, encoding="utf-8") as file:
            raw = json.load(file)

    elif settings.DATA_SOURCE == "excel":
        # row 1 = column names, row 2 = the values for this run
        sheet = load_workbook(settings.EXCEL_FILE, data_only=True)[settings.EXCEL_SHEET]
        headers = [cell.value for cell in sheet[1]]
        values = [cell.value for cell in sheet[2]]
        raw = dict(zip(headers, values))

    else:
        raise ValueError("DATA_SOURCE must be 'json' or 'excel'")

    # Excel can hand back numbers where we expect text, so turn everything
    # into text first and then convert only the quantity back to a number
    data = {key: str(value).strip() for key, value in raw.items()}
    data["new_quantity"] = int(float(data["new_quantity"]))
    return data


# ---------------------------------------------------------------------
# TASK 1 - launch browser
# ---------------------------------------------------------------------
def start_browser():
    browser = settings.BROWSER.lower()

    if browser == "chrome":
        options = ChromeOptions()
        # "ignore" = the browser must not auto-close alerts, so that
        # handle_alert_if_present() can read them first (task 9)
        options.set_capability("unhandledPromptBehavior", "ignore")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )

    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_capability("unhandledPromptBehavior", "ignore")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )

    else:
        raise ValueError("BROWSER must be 'chrome' or 'firefox'")

    driver.maximize_window()
    driver.implicitly_wait(settings.IMPLICIT_WAIT)
    return driver


# ---------------------------------------------------------------------
# TASK 7 - capture screenshots
# ---------------------------------------------------------------------
def take_screenshot(driver, name):
    os.makedirs(settings.SCREENSHOT_FOLDER, exist_ok=True)

    file_name = datetime.now().strftime("%H%M%S") + "_" + name + ".png"
    driver.save_screenshot(os.path.join(settings.SCREENSHOT_FOLDER, file_name))

    screenshots_taken.append(file_name)
    print("   screenshot saved:", file_name)


# ---------------------------------------------------------------------
# TASK 9 - handle popups / alerts if they appear
# ---------------------------------------------------------------------
def handle_alert_if_present(driver):
    # a real browser alert (window.alert / confirm)
    try:
        alert = driver.switch_to.alert
        print("   browser alert found:", alert.text)
        alert.accept()
        return True
    except NoAlertPresentException:
        return False


def close_banner(driver):
    # the green/red bar after add-to-cart or a cart update is not a browser
    # alert, it is part of the page, so it is closed by clicking its "x"
    for close_button in driver.find_elements(By.CSS_SELECTOR, ".alert .close"):
        if close_button.is_displayed():
            close_button.click()


# ---------------------------------------------------------------------
# small utilities
# ---------------------------------------------------------------------
def price_to_number(text):
    # "$1,202.00" -> 1202.0
    return float(text.replace("$", "").replace(",", "").strip())


def log_result(step, status, note=""):
    results.append((step, status, note))
    print(status, "-", step, note)


# ---------------------------------------------------------------------
# TASK 10 - execution report (a plain html file)
# ---------------------------------------------------------------------
def write_report():
    os.makedirs(settings.REPORT_FOLDER, exist_ok=True)
    report_name = "execution_report_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".html"

    rows = ""
    for step, status, note in results:
        color = "#1a7f37" if status == "PASS" else "#cf222e"
        rows += (
            f"<tr><td>{step}</td>"
            f"<td style='color:{color};font-weight:bold'>{status}</td>"
            f"<td>{note}</td></tr>\n"
        )

    # the report sits in reports/, the images in screenshots/, hence the ../
    pictures = ""
    for file_name in screenshots_taken:
        pictures += (
            f"<p>{file_name}<br>"
            f"<img src='../screenshots/{file_name}' width='700'></p>\n"
        )

    passed = sum(1 for item in results if item[1] == "PASS")
    html = f"""<html>
<head><title>Execution Report</title></head>
<body style="font-family:Arial">
<h2>TutorialsNinja purchase flow - execution report</h2>
<p>Run time: {datetime.now():%Y-%m-%d %H:%M:%S} | Browser: {settings.BROWSER} | Data: {settings.DATA_SOURCE}</p>
<p>{passed} of {len(results)} steps passed</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Step</th><th>Status</th><th>Notes</th></tr>
{rows}</table>
<h3>Screenshots</h3>
{pictures}
</body></html>"""

    report_path = os.path.join(settings.REPORT_FOLDER, report_name)
    with open(report_path, "w", encoding="utf-8") as file:
        file.write(html)
    print("Report written:", report_path)
