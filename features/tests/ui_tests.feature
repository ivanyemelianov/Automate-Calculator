# Created by dariasamarets at 2021-02-26
Feature: Check if every text on the screen is correct
  # Enter feature description here

  Scenario: Every digit button displays its digit
    Given Application is running
    When Main page is open
    Then Text of the button is set correctly

  Scenario: Modes are named correctly
    Given Application is running
    When Main page is open
    Then Text of DEG mode is set correctly
    When Change mode
    Then Text of RAD mode is set correctly
