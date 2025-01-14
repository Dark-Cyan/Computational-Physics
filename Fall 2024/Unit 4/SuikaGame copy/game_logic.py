#game_logic.py

import time



class Game:

    #Constructor for the game class
    def __init__(self):
        global loseTimer
        self.state='play'
        self.score=0
        self.loseTimer = time.time()

    #Sets game object back to initial state
    def reset(self):
        self.state='play'
        self.score = 0
        self.loseTimer = time.time()

    #update timer depending on if a ball is out of the play space
    def overFlow(self, on):

        if on: #if there is something overflowing, do not update loseTimer
            hello = 1
        else: #if there is nothing overflowing, update loseTimer
            self.loseTimer = time.time()
        self.lose()

    #updates points
    def updatePoints(self, list):
        self.points = sum(list)

    #set state to win
    def win(self):
        self.state='win'

    #determines if the game is lost
    def lose(self):
        if (time.time() - self.loseTimer >= 5): #if 5 seconds have passed with an object overflowing set state to lose
            self.state='lose'
            