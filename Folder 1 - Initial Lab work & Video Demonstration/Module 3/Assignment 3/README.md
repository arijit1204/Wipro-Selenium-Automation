# Assignment 3 - Selenium Page Object Model in Python Behave

## Objective

Debug and optimize web application automation using the Behave framework, Gherkin, Selenium and the Page Object Model design pattern.

## Tools

- Python
- Behave
- Selenium
- PyCharm Community
- Chrome / ChromeDriver

## Project Structure

Assignment_3_Selenium_POM_Behave/
    features/
        login.feature
        environment.py
        pages/
            login_page.py
            inventory_page.py
        steps/
            login_steps.py
    requirements.txt
    README.md

## Installation

Run:

python -m pip install -r requirements.txt

## Run

From the Assignment_3_Selenium_POM_Behave folder:

python -m behave

## Design

LoginPage contains:
- Login locators
- Open page method
- Username method
- Password method
- Login method
- Error message method

InventoryPage contains:
- Inventory page validation method

The step definitions contain the test flow.

The feature file contains the test data using Scenario Outline and Examples.

Assertions are kept in the step definitions and are separate from page locators.

## Test Data

The feature executes four combinations:

1. Correct username + correct password
2. Incorrect username + correct password
3. Correct username + incorrect password
4. Incorrect username + incorrect password

## Expected Result

4 scenarios passed.
