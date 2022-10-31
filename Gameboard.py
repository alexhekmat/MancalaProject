class Gameboard:

    ## This constructor will construct the player objects and set them to whichever players are playing
    ## Param: p1 is a player object
    ## Param: p2 is a player object
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2

    ##This method will sow the seed from whichever hole the player chooses
    ## Param: p1 is a player object
    ## Param: p2 is a player object
    ## Param: choice is an int indicating which hole
    def sow_seed(self, p1, p2, choice):
        ## Checks if they chose the right hole or the left hole using the int 0 or 1
        if choice == 0:
            seeds = p1.get_right()
            p1.empty_hole(choice)
            ## Runs the while until seeds = 0
            while seeds > 0:
                p2.change_left_hole()
                seeds = seeds - 1
                ## Runs in a counter clockwise order for each hole using an if to determine if
                ## it should be placed in the hole
                if seeds > 0:
                    p2.change_right_hole()
                    seeds = seeds - 1
                ## Runs in a counter clockwise order for each hole using an if to determine if
                ## it should be placed in the hole
                if seeds > 0:
                    p1.change_left_hole()
                    seeds = seeds - 1
                ## Runs in a counter clockwise order for each hole using an if to determine if
                ## it should be placed in the hole
                if seeds > 0:
                    p1.change_right_hole()
                    seeds = seeds - 1
        else:
            seeds = p1.get_left()
            p1.empty_hole(choice)
            ## Runs the while until seeds = 0
            while seeds > 0:
                p1.change_right_hole()
                seeds = seeds - 1
                ## Runs in a counter clockwise order for each hole using an if to determine
                ## if it should be placed in the hole
                if seeds > 0:
                    p2.change_left_hole()
                    seeds = seeds - 1
                ## Runs in a counter clockwise order for each hole using an if to determine
                ## if it should be placed in the hole
                if seeds > 0:
                    p2.change_right_hole()
                    seeds = seeds - 1
                ## Runs in a counter clockwise order for each hole using an if to determine
                ## if it should be placed in the hole
                if seeds > 0:
                    p1.change_left_hole()
                    seeds = seeds - 1


    ## This method checks if the player parameters holes both have zero seeds in them,
    ## if it returns false they do, if not true
    ## Param: player is a player object
    ## Returns: a boolean either True or False
    def checks_winner(self, player):
        ## Checks if the players right and left holes are both zero,
        ## returns false if they are both 0, and true if they are not
        if (player.get_right() == 0) and (player.get_left() == 0):
            return False
        else:
            return True

    ## This method prints the 2 arrays to print the board showcasing it from a top-down view
    ## Param: player1 is a player object
    ## Param: player2 is a player object
    def print_board(self, player1, player2):
        print([player1.get_right(), player1.get_left()])
        print([player2.get_left(), player2.get_right()])
