from Human import Human
from Gameboard import Gameboard

player1 = Human()
player2 = Human()
gameboard = Gameboard(player1, player2)

gameboard.print_board(player1, player2)


while (gameboard.checks_winner(player1)) and (gameboard.checks_winner(player2)):
    while seeds == 0:
         print("Invalid choice, pick hole again")
    if gameboard.checks_winner(player1):
        choice = player1.choose_hole()
        gameboard.sow_seed(player1, player2, choice)
        gameboard.print_board(player1, player2)
    else:
        print("Player 2 Wins")
    while seeds == 0:
        ("Invalid choice, pick hole again")
    if gameboard.checks_winner(player2):
        choice = player2.choose_hole()
        gameboard.sow_seed(player2, player1, choice)
        gameboard.print_board(player1, player2)
    else:
        print("Player 2 Wins")
