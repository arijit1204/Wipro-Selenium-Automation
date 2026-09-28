*** Settings ***
Library    SeleniumLibrary
Resource   keywords.resource
Test Template    Login With Credentials
Suite Setup      Open Login Page
Suite Teardown   Close All Browsers

*** Variables ***
${URL}        https://www.saucedemo.com/
${BROWSER}    Chrome

*** Test Cases ***    ${username}    ${password}    ${expected}
Valid Login          standard_user    secret_sauce    success
Invalid Username     wrong_user       secret_sauce    error
Invalid Password     standard_user    wrong_password  error
Invalid Credentials  wrong_user      wrong_password  error

*** Keywords ***
Login With Credentials
    [Arguments]    ${username}    ${password}    ${expected}
    Go To    ${URL}
    Wait Until Page Contains Element    id=user-name
    Enter Username    ${username}
    Enter Password    ${password}
    Click Login
    Verify Login Result    ${expected}
