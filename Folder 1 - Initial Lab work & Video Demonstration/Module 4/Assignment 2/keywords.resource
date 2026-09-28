*** Keywords ***
Open Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    5s

Enter Username
    [Arguments]    ${username}
    Input Text    id=user-name    ${username}

Enter Password
    [Arguments]    ${password}
    Input Text    id=password    ${password}

Click Login
    Click Button    id=login-button
    Sleep    5s

Verify Login Result
    [Arguments]    ${expected}
    IF    '${expected}' == 'success'
        Page Should Contain Element    id=inventory_container
    ELSE
        Page Should Contain Element    css=[data-test="error"]
    END
