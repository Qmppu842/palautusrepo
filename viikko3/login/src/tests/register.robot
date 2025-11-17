*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  lohi
    Set Password  kala12345
    Set Confirmation  kala12345

Register With Too Short Username And Valid Password
    Set Username  lo
    Set Password  kala12345
    Set Confirmation  kala12345
    Register Should Fail With Message  You too short, go grow some.


Register With Valid Username And Too Short Password
    Set Username  lohi2
    Set Password  kala12
    Set Confirmation  kala12
    Register Should Fail With Message  Your secret must be at least 8 chars long to enter this ride.

Register With Valid Username And Invalid Password
    Set Username  lohi3
    Set Password  kalakoira
    Set Confirmation  kalakoira
    Register Should Fail With Message  Invalid password, add something like at least 8 chars and some other chars than alphabets too. Or don't, I am not your boss.

Register With Nonmatching Password And Password Confirmation
    Set Username  lohi4
    Set Password  kala12345
    Set Confirmation  automyynti12
    Register Should Fail With Message  Password and confirmation does not match

Register With Username That Is Already In Use
    Set Username  lohi
    Set Password  kala12345
    Set Confirmation  kala12345
    Register Should Fail With Message  User name already in use

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

*** Keywords ***

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}