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

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Login Page Should Be Open

Login Page Should Be Open
    Title Should Be     Login

Go To Login Page
    Go To   ${LOGIN_URL}
    Login Page Should Be Open


Input Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text  password    ${password}

Submit Credentials
    Click Button    Login

Current Page Should Be Open
    Location Should Be    ${CURRENT_URL}
    Title Should Be     Current
