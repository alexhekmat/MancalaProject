class Gameboard:

    def __init__(self,p1,p2):
        self.player1 = p1
        self.player2 = p2

    def sow_seed(self, player):
    def checks_winner(self, player):
        if ( player.get_Right() == 0) and (player.get_left() == 0):
            return "no move"
    def print_board(self, player1, player2):
        print([player1.get_right(), player1.get_left()])
        print([player2.get_left(), player2.get_left()])
