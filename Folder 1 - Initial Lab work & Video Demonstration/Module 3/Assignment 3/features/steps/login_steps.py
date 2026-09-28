from behave import given, when, then
from features.pages.login_page import LoginPage
from features.pages.inventory_page import InventoryPage

@given("I open the SauceDemo login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.inventory_page = InventoryPage(context.driver)
    context.login_page.open()

@when('I enter username "{username}"')
def step_enter_username(context, username):
    context.login_page.enter_username(username)

@when('I enter password "{password}"')
def step_enter_password(context, password):
    context.login_page.enter_password(password)

@when("I click the login button")
def step_click_login(context):
    context.login_page.click_login()

@then('the login result should be "{result}"')
def step_verify_login_result(context, result):
    if result == "success":
        assert context.inventory_page.is_open()
    else:
        assert context.login_page.get_error_message() != ""
