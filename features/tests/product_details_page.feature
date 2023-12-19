Feature: Test Scenarios for Reelly - Product Details Page

  Scenario: 26 - User can open product detail and see three options of visualization
    Given Open the main page.
    And Log in to the page.
    When Click on “off plan” at the left side menu.
    And Click on the first product.
    Then Verify the three options of visualization are “architecture”, “interior”, “lobby”
    And Verify the visualization options are clickable.
