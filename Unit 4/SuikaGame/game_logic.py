#game_logic.py

import time



class Game:

    #Timers

    def __init__(self):
        global loseTimer
        self.state='play'
        self.score=0
        self.loseTimer = time.time()

    def reset(self):
        self.state='play'
        self.score = 0
        self.loseTimer = time.time()

    def overFlow(self, on):
        if on:
            hello = 1
        else:
            self.loseTimer = time.time()
        self.lose()

    def updatePoints(self, list):
        points = sum(list)

    def win(self):
        self.state='win'

    def lose(self):
        if (time.time() - self.loseTimer >= 5):
            self.state='lose'
            