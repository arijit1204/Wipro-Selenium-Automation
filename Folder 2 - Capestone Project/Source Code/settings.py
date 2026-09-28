# settings.py
# Every value that might change lives in this file. The other files only
# read from here, so switching browser or data file never touches the logic.

import os

# ---- what to run ----
BROWSER = "chrome"          # "chrome" or "firefox"
DATA_SOURCE = "json"        # "json" or "excel"
BASE_URL = "https://tutorialsninja.com/demo/"

# ---- timing, in seconds ----
IMPLICIT_WAIT = 10          # how long find_element keeps looking before it fails
PAUSE = 2                   # short pause after page changes so the page settles

# ---- folders and files ----
# built from this file's own location, so the project runs from any folder
PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(PROJECT_FOLDER, "data")
SCREENSHOT_FOLDER = os.path.join(PROJECT_FOLDER, "screenshots")
REPORT_FOLDER = os.path.join(PROJECT_FOLDER, "reports")

JSON_FILE = os.path.join(DATA_FOLDER, "test_data.json")
EXCEL_FILE = os.path.join(DATA_FOLDER, "test_data.xlsx")
EXCEL_SHEET = "TestData"    # sheet name inside the Excel file
