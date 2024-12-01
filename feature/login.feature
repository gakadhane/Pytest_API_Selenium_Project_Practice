Feature: validation of orange HRM login
  Scenario: login with valid creds
    Given open browser
    When enter user name "Admin" passwords "admin123"
    Then click login button
    And Home page loaded successfully