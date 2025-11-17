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
    Click Button  Register
    User Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  lo
    Set Password  kala12345
    Set Confirmation  kala12345
    Click Button  Register
    Register Should Fail With Message  You too short, go grow some.


Register With Valid Username And Too Short Password
    Set Username  lohi2
    Set Password  kala12
    Set Confirmation  kala12
    Click Button  Register
    Register Should Fail With Message  Gotta be better person, wink wink, if you know, you know, but now, you dont pass

Register With Valid Username And Invalid Password
    Set Username  lohi3
    Set Password  kalakoira
    Set Confirmation  kalakoira
    Click Button  Register
    Register Should Fail With Message  Invalid password, add something like at least 8 chars and some other chars than alphabets too. Or don't, I am not your boss.

Register With Nonmatching Password And Password Confirmation
    Set Username  lohi4
    Set Password  kala12345
    Set Confirmation  automyynti12
    Click Button  Register
    Register Should Fail With Message  Password and confirmation does not match

Register With Username That Is Already In Use
    Set Username  lohi
    Set Password  kala1234544
    Set Confirmation  kala1234544
    Click Button  Register

    Go To Register Page

    Set Username  lohi
    Set Password  kala1234544
    Set Confirmation  kala1234544
    Click Button  Register
    Register Should Fail With Message  User with username lohi already exists

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