*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://www.saucedemo.com/
${BROWSER}    Chrome

*** Test Cases ***
Open Browser And Navigate
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Page Should Contain    Swag Labs
    Input Text    id=user-name    standard_user
    Input Text    id=password    secret_sauce
    Page Should Contain Element    id=user-name
    Page Should Contain Element    id=password
    Close Browser