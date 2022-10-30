from Human import Human
from Gameboard import Gameboard

player1 = Human()
player2 = Human()
gameboard = Gameboard(player1, player2)
print("The Mini Mancala board is viewed from a top down angle, therefore the first player "
      "views the top half of the board reversed")
gameboard.print_board(player1, player2)

## While loop runs with an or because there is a break within the winner, instead of an and, so it runs until reaching the break
while (gameboard.checks_winner(player1)) or (gameboard.checks_winner(player2)):
    ## Checks if the player1 holes still have seeds by calling checking winner, else it prints that the second player won and breaks
    if gameboard.checks_winner(player1):
        print("First Player Choose a Hole!")
        choice = player1.choose_hole()
        ## While loop in order to check if there are seeds in the hole
        while choice == 0 and player1.get_right() == 0:
            print("Invalid choice, pick hole again")
            choice = player1.choose_hole()
        ## While loop in order to check if there are seeds in the other hole
        while choice == 1 and player1.get_left() == 0:
            print("Invalid choice, pick hole again")
            choice = player1.choose_hole()
        gameboard.sow_seed(player1, player2, choice)
        gameboard.print_board(player1, player2)
    else:
        print("Second Player Wins")
        break
    ## Checks if the player2 holes still have seeds by calling checking winner, else it prints that the first player won and breaks
    if gameboard.checks_winner(player2):
        print("Second Player Choose a Hole!")
        choice = player2.choose_hole()
        ## While loop in order to check if there are seeds in the hole
        while choice == 0 and player2.get_right() == 0:
            print("Invalid choice, pick hole again")
            choice = player2.choose_hole()
        ## While loop in order to check if there are seeds in the other hole
        while choice == 1 and player2.get_left() == 0:
            print("Invalid choice, pick hole again")
            choice = player1.choose_hole()
        gameboard.sow_seed(player2, player1, choice)
        gameboard.print_board(player1, player2)
    else:
        print("First Player Wins")
        break
