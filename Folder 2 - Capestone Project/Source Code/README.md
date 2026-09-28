# TutorialsNinja Purchase Flow - Selenium WebDriver + Python

Capstone Assignment 1. The script plays a customer on
https://tutorialsninja.com/demo/ : it registers, logs in, searches for a
product, adds it to the cart, changes the quantity and verifies the cart.
Every step takes a screenshot, the test data comes from a JSON or Excel file,
alerts are handled, and a HTML report is written at the end.

## File structure

```
capstone_project/
|-- main.py                 run this file - the purchase flow, step by step
|-- settings.py             browser, data source, URL, waits, folder paths
|-- helpers.py              reusable functions used by main.py
|-- requirements.txt        packages to install
|-- README.md               this file
|-- video_script.txt        line-by-line explanation script for the video
|-- data/
|   |-- test_data.json      test data (JSON version)
|   `-- test_data.xlsx      same test data (Excel version, sheet "TestData")
|-- screenshots/            created on the first run, one PNG per step
`-- reports/                created on the first run, one HTML report per run
```

## Setup and run

```
pip install -r requirements.txt
python main.py
```

Needs Python 3.9+ and Chrome (or Firefox). `webdriver-manager` downloads the
matching driver on the first run, so an internet connection is required.

To change how it runs, edit `settings.py`:

| Setting       | Values              | Effect                          |
|---------------|---------------------|---------------------------------|
| `BROWSER`     | `"chrome"` / `"firefox"` | which browser is started   |
| `DATA_SOURCE` | `"json"` / `"excel"`     | which data file is read    |
| `PAUSE`       | seconds             | pause after page changes        |

## What each file does

**settings.py** - only constants. Nothing runs in this file. Folder paths are
built from the file's own location, so the project works from any directory.

**helpers.py** - the small reusable jobs:

| Function                   | Task | What it does                                             |
|----------------------------|------|----------------------------------------------------------|
| `read_test_data()`         | 8    | reads JSON or Excel and returns one dictionary           |
| `start_browser()`          | 1    | starts Chrome or Firefox, maximizes, sets the implicit wait |
| `take_screenshot()`        | 7    | saves a PNG in `screenshots/` and remembers its name     |
| `handle_alert_if_present()`| 9    | accepts a browser alert if there is one                  |
| `close_banner()`           | 9    | closes the green/red bar shown after cart actions        |
| `price_to_number()`        |      | turns `"$1,202.00"` into `1202.0`                        |
| `log_result()`             | 10   | records a step as PASS/FAIL for the report               |
| `write_report()`           | 10   | writes the HTML report into `reports/`                   |

**main.py** - one function, `main()`, with the steps in order. It is wrapped
in `try / except / finally`: if a step fails, the `except` block records which
one and takes a failure screenshot, and the `finally` block always closes the
browser and writes the report.

## Where each assignment task is done

| # | Task                      | Where                                              |
|---|---------------------------|----------------------------------------------------|
| 1 | Launch browser            | `start_browser()` in helpers.py, called in main.py |
| 2 | Login                     | "TASK 2" block in main.py                          |
| 3 | Search product            | "TASK 3" block in main.py                          |
| 4 | Add product to cart       | "TASK 4" block in main.py                          |
| 5 | Update quantity           | "TASK 5" block in main.py                          |
| 6 | Verify cart details       | "TASK 6" block in main.py                          |
| 7 | Capture screenshots       | `take_screenshot()`, called after every step       |
| 8 | Read test data            | `read_test_data()` in helpers.py                   |
| 9 | Handle popups / alerts    | `handle_alert_if_present()`, `close_banner()`      |
| 10| Execution report          | `write_report()` in helpers.py                     |

## Test data

| Field            | Meaning                                                   |
|------------------|-----------------------------------------------------------|
| `first_name`, `last_name`, `telephone`, `password` | used for registration and login |
| `email_template` | `{stamp}` is replaced by the current time on every run    |
| `search_keyword` | typed into the search box                                 |
| `product_name`   | exact product title expected in the results and the cart  |
| `new_quantity`   | quantity set in the cart, must be 2 or more               |

The Excel file has the same columns: row 1 = names, row 2 = values.

## Output

- `screenshots/` - `HHMMSS_<step>.png`, one per step
- `reports/execution_report_<date_time>.html` - step table (PASS/FAIL, notes) and all screenshots

## Notes

- The demo site has no shared login, so each run registers a new customer
  (email built from the current time), logs out, and then logs in with it.
- If the site changes its page layout, the locators (`By.ID`, CSS and XPath
  strings) in `main.py` are the only lines that need editing.
