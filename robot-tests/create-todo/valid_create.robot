*** Settings ***
Documentation     A test suite with a single test for valid create todo.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

*** Test Cases ***
Valid Create
    Open Browser To Login Page
    Input Username  manologonz
    Input Password  12345678
    Submit Credentials
    Current Page Should Be Open
    Go To Create Todo
    Input Title     Robot Todo
    Input Memo      Is a todo by robot
    Submit Create To Do
    Current Page Should Be Open
    [Teardown]  Close Browser
