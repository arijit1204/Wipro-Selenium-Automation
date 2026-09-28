Feature: API Automation

  Scenario Outline: Validate GET API with different test data
    Given I send a GET request to "<endpoint>"
    Then the response status code should be <status_code>
    And the response should contain "<field>"

    Examples:
      | endpoint | status_code | field |
      | /posts/1 | 200 | userId |
      | /posts/2 | 200 | userId |
      | /posts/3 | 200 | userId |

  Scenario Outline: Create a new post using test data
    Given I send a POST request with title "<title>" and body "<body>"
    Then the response status code should be 201
    And the response should contain title "<title>"

    Examples:
      | title | body |
      | Test Post 1 | Automation Testing |
      | Test Post 2 | Python Behave API |
      | Test Post 3 | API Automation |
