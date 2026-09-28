import requests
from behave import given, then

BASE_URL = "https://jsonplaceholder.typicode.com"

@given('I send a GET request to "{endpoint}"')
def step_get_request(context, endpoint):
    context.response = requests.get(BASE_URL + endpoint)

@then("the response status code should be {status_code:d}")
def step_status_code(context, status_code):
    assert context.response.status_code == status_code

@then('the response should contain "{field}"')
def step_response_contains_field(context, field):
    data = context.response.json()
    assert field in data

@given('I send a POST request with title "{title}" and body "{body}"')
def step_post_request(context, title, body):
    payload = {
        "title": title,
        "body": body,
        "userId": 1
    }

    context.response = requests.post(
        BASE_URL + "/posts",
        json=payload
    )

@then('the response should contain title "{title}"')
def step_response_contains_title(context, title):
    data = context.response.json()
    assert data["title"] == title
