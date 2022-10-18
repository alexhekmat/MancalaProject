class Gameboard:

    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2

    def sow_seed(self, p1, p2):
        self.print_board(p2)
        if whichHole == 0:
            seeds = p1.get_right(p1)
            while seeds > 0:
                p2.change_left_hole(p1)
                seeds = seeds - 1
                if seeds > 0:
                    p2.change_right_hole(p1)
                    seeds = seeds - 1
                if seeds > 0:
                    p1.change_left_hole(p1)
                    seeds = seeds - 1
                if seeds > 0:
                    p1.change_right_hole(p1)
                    seeds = seeds - 1
        else:
            seeds = self.get_left(self)
            while seeds > 0:
                self.change_right_hole(self)
                seeds = seeds - 1
                if seeds > 0:
                    p2.change_left_hole(self)
                    seeds = seeds - 1
                if seeds > 0:
                    p2.change_right_hole(self)
                    seeds = seeds - 1
                if seeds > 0:
                    self.change_left_hole(self)
                    seeds = seeds - 1
    def checks_winner(self, player):
        if ( player.get_Right() == 0) and (player.get_left() == 0):
            return "no move"
    def print_board(self, player2):
        print([self.get_right(), self.get_left()])
        print([player2.get_left(), player2.get_left()])
