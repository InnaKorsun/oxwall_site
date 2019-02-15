Feature: Status feature
  Description: User can add a status with photo and without photo on Dashboard page
  or on Main page.
  The status appears on page in few seconds after posting without page reloading.
  User can delete status added by him. Only admin can delete every news.

  Scenario Outline: Add text status (without photo)
    Given initial amount of status in Oxwall database
    Given I as a logged user
    When I add a status with <text> in Dashboard page
    Then a new status block appears before old list of status
    Then this status block has this <text> and author as this user and time "within 1 minute"

    Examples:
    | text                |
    | !@#%^&              |
    | New 1234098765!     |
    | Привіт!             |