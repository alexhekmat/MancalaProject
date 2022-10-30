class Player:

    ##This constructor will construct the amount of seeds in each hole for the player
    def __init__(self):
        self.hole_right = 2
        self.hole_left = 2

    ##this method will access the amount of seeds in the right hole
    def get_right(self):
        return self.hole_right

    ##This method will access the amount of seeds in the left hole
    def get_left(self):
        return self.hole_left

    ## This method will change the amount of seeds in the right hole by +1
    def change_right_hole(self):
        self.hole_right = self.hole_right + 1

    ## This method will change the amount of seeds in the left hole by +1
    def change_left_hole(self):
        self.hole_left = self.hole_left + 1

    ## This method will empty the hole that the user chooses to play
    def empty_hole(self, choice):
        if choice == 0:
            self.hole_right = 0
        else:
            self.hole_left = 0

    ## This method will return an int that represents which hole the user would like to play
    ## 0 represents the player's right hole 1 represents the player's left hole
    def choose_hole(self):
        whichHole = int(input("Do you want your Right hole (0) or your Left hole (1)?"))
        return whichHole
