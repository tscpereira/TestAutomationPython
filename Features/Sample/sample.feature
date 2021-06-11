Feature: Test Web Page / Google API


  @TestSample001 @All
  Scenario: Test Google API
    Given I need run a get at google API

  @TestSample002 @All @UI
  Scenario Outline: Search on Google
     Given Im in the google page
      When Search by "<item>"
      Then Check the results for "<item>"

     Examples: item
       | item      |
       | Selenium  |
       | Python    |
       | Behave    |

  @TestSample003 @All @UI-APP-MOBILE
  Scenario: Test App Login
    Given I need to perform login in a mobile application