*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${SERVER}   localhost:8000
${BROWSER}  Firefox
${DELAY}    1
${VALID_USER}   manologonz
${VALID_PASSWORD}   12345678
${LOGIN_URL}    http://${SERVER}/login/
${CURRENT_URL}     http://${SERVER}/current/
${CREATE_URL}   http://${SERVER}/create/

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Login Page Should Be Open

Login Page Should Be Open
    Title Should Be     Login

Create Page Should Be Open
    Title Should Be     New Todo

Go To Login Page
    Go To   ${LOGIN_URL}
    Login Page Should Be Open

Go To Create Todo
    Go To   ${CREATE_URL}
    Create Page Should Be Open

Input Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text  password    ${password}

Input Title
    [Arguments]    ${title}
    Input Text    title    ${title}

Input Memo
    [Arguments]    ${memo}
    Input Text    memo    ${memo}

Submit Credentials
    Click Button    Login

Submit Create To Do
    Click Button    Save

Current Page Should Be Open
    Location Should Be    ${CURRENT_URL}
    Title Should Be     Current
