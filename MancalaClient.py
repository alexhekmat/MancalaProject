from Human import Human
from Gameboard import Gameboard

player1 = Human()
player2 = Human()
gameboard = Gameboard(player1, player2)

gameboard.print_board(player1, player2)


while (gameboard.checks_winner(player1)) and (gameboard.checks_winner(player2)):

    if gameboard.checks_winner(player1):
        choice = player1.choose_hole()
        while choice == 0 and player1.get_right() == 0:
            print("Invalid choice, pick hole again")
            choice = player1.choose_hole()
        while choice == 1 and player1.get_left() == 0:
            print("Invalid choice, pick hole again")
            choice = player1.choose_hole()
        gameboard.sow_seed(player1, player2, choice)
        gameboard.print_board(player1, player2)
    else:
        print("Player 2 Wins")
    if gameboard.checks_winner(player2):
        choice = player2.choose_hole()
        while choice == 0 and player2.get_right() == 0:
            print("Invalid choice, pick hole again")
            choice = player2.choose_hole()
        while choice == 1 and player2.get_left() == 0:
            print("Invalid choice, pick hole again")
            choice = player1.choose_hole()
        gameboard.sow_seed(player2, player1, choice)
        gameboard.print_board(player1, player2)
    else:
        print("Player 2 Wins")
