Feature: Cocktail Ordering

  As Romeo, I want to offer a drink to Juliette so that we can discuss together.

  Scenario Outline: Creating an empty order
    Given <from> who wants to buy a drink
    When  an order is declared for <to>
    Then  there is <nbDrinks> cocktails in the order

    Examples:
          | from  | to       | nbDrinks    |
          | Romeo | Juliette |           0 |
          | Tom   | Jerry    |           0 |
