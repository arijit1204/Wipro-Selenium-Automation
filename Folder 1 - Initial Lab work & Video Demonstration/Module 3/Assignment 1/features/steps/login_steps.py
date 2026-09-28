from behave import given, when, then
from src.application import Application

@given("the application is running")
def step_application_running(context):
    context.application = Application()
    context.application.start()

@when("I enter a valid username")
def step_valid_username(context):
    context.application.enter_username("admin")

@when("I enter a valid password")
def step_valid_password(context):
    context.application.enter_password("admin123")

@when("I enter an invalid username")
def step_invalid_username(context):
    context.application.enter_username("wrong_user")

@when("I enter an invalid password")
def step_invalid_password(context):
    context.application.enter_password("wrong_password")

@when("I click the login button")
def step_login(context):
    context.application.login()

@then("I should see the dashboard")
def step_dashboard(context):
    assert context.application.current_page == "dashboard"

@then("I should see the login error")
def step_login_error(context):
    assert context.application.current_page == "login"
    assert context.application.error_message == "Invalid username or password"
