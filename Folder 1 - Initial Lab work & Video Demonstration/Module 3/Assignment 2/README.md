# Assignment 2 - Test Data Driven API Automation

## Objective

Perform API automation using Python and the Behave BDD framework with multiple test-data combinations.

## Tools

- Python
- Behave
- Requests
- PyCharm Community

## Project Structure

Assignment_2_API_Behave/
    features/
        api_automation.feature
        steps/
            api_steps.py
    requirements.txt
    README.md

## Installation

Open the PyCharm terminal and run:

python -m pip install -r requirements.txt

## Run the Tests

From the Assignment_2_API_Behave folder:

python -m behave

## What the project demonstrates

- Behave BDD framework
- API automation using Python Requests
- Scenario Outline
- Examples table for test data
- GET API testing
- POST API testing
- Status code validation
- Response field validation
- Response value validation

## API Used

JSONPlaceholder is used as a public practice REST API.

GET endpoints:
https://jsonplaceholder.typicode.com/posts/1
https://jsonplaceholder.typicode.com/posts/2
https://jsonplaceholder.typicode.com/posts/3

POST endpoint:
https://jsonplaceholder.typicode.com/posts

## Expected Result

The feature executes multiple GET and POST test-data combinations through the Behave Scenario Outline mechanism.
