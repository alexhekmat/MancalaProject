class Gameboard:

    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2

    def sow_seed(self, p1, p2, choice):
        if choice == 0:
            seeds = p1.get_right()
            p1.empty_hole(choice)
            while seeds > 0:
                p2.change_left_hole()
                seeds = seeds - 1
                if seeds > 0:
                    p2.change_right_hole()
                    seeds = seeds - 1
                if seeds > 0:
                    p1.change_left_hole()
                    seeds = seeds - 1
                if seeds > 0:
                    p1.change_right_hole()
                    seeds = seeds - 1
        else:
            seeds = p1.get_left()
            if seeds == 0:
                print("Invalid choice, pick hole again")
                return
            p1.empty_hole(choice)
            while seeds > 0:
                p1.change_right_hole()
                seeds = seeds - 1
                if seeds > 0:
                    p2.change_left_hole()
                    seeds = seeds - 1
                if seeds > 0:
                    p2.change_right_hole()
                    seeds = seeds - 1
                if seeds > 0:
                    p1.change_left_hole()
                    seeds = seeds - 1

    ## if False is returned than the player has lost, if True is returned then continue play
    def checks_winner(self, player):
        if (player.get_right() == 0) and (player.get_left() == 0):
            return False
        else:
            return True

    def print_board(self, player1, player2):
        print([player1.get_right(), player1.get_left()])
        print([player2.get_left(), player2.get_right()])
