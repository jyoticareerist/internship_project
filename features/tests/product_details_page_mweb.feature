Feature: Test Scenarios for Reelly - Product Details Page for Mobile Web

  Scenario: 26 - User can open product detail and see three options of visualization
    Given Open the main page.
    And Log in to the page.
    When Click on “off plan” in the bottom menu.
    And Click on the first product.
    Then Verify the three options of visualization are “architecture”, “interior”, “lobby”
    And Verify the visualization options are clickable.
