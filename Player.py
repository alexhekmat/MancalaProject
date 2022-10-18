class Player:


    ##This constructor will construct the amount of seeds in each hole for the player
    def __init__(self):
        self.hole_right = 2
        self.hole_left = 2
        self.gameboard = [self.hole_right, self.hole_left]

    ##this method will access the amount of seeds in the right role
    def get_right(self):
        return self.hole_right
    ##This method will access the amount of seeds in the left hole

    def get_left(self):
        return self.hole_left
    ##This method will access and return the gameboard

    def get_gameboard(self):
        return self.gameboard
    ## This method will mutate the amount of seeds in the right hole

    def change_right_hole(self):
        self.hole_right = self.hole_right + 1
    ## This method will mutate the amount of seeds in the left hole

    def change_left_hole(self):
        self.hole_left = self.hole_left + 1

    def choose_hole(self):
        whichHole = input("Do you want hole Right (0) or hole Left (1)?")
        return int(whichHole)