Feature: User Login

  Scenario: Successful login
    Given the application is running
    When I enter a valid username
    And I enter a valid password
    And I click the login button
    Then I should see the dashboard

  Scenario: Invalid login
    Given the application is running
    When I enter an invalid username
    And I enter an invalid password
    And I click the login button
    Then I should see the login error
