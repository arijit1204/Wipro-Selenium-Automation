Feature: SauceDemo Login

  Scenario Outline: Login with different test data
    Given I open the SauceDemo login page
    When I enter username "<username>"
    And I enter password "<password>"
    And I click the login button
    Then the login result should be "<result>"

    Examples:
      | username      | password      | result  |
      | standard_user | secret_sauce  | success |
      | wrong_user    | secret_sauce  | error   |
      | standard_user | wrong_password | error   |
      | wrong_user    | wrong_password | error   |
