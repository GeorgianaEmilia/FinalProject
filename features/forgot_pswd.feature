Feature: Jules forgot password tests

    #se ruleaza inainte de fiecare test(in general given urile)
  Background:
    Given sign_in: I am a user on Jules sign in page

  @jules1
  Scenario: Wrong email validation message
    When sign_in: I click forgot password link
    When forgot_pswd: I set my email "abcd"
    Then forgot_pswd: I verify that email validation is correct


  @jules
  Scenario Outline: Wrong email validation message with table data
    When sign_in: I click forgot password link
    When forgot_pswd: I set my email "<email>"
    Then forgot_pswd: I verify that email validation is correct
    Examples:
      | email      |
      | abcdfasafa |
      | gggdd.rdam |
