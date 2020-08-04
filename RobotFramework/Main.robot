*** Settings ***
Documentation                   Suite description
Library                         SeleniumLibrary
Library                         Screenshot
Library                         OperatingSystem
Resource                        variables.robot
Test Setup                      Start web-browser
Test Teardown                   Close web-browser

*** Test Cases ***
TC01
    Go to                       https://www.alza.cz/

*** Keywords ***
Start web-browser
    Open Browser                ${URL}      ${BROWSER}
Close web-browser
    Close Browser