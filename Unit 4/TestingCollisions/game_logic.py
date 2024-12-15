#game_logic.py

import time



class Game:

    #Timers

    def __init__(self):
        global loseTimer
        self.state='play'
        self.score=0
        self.loseTimer = time.time()

    def overFlow(self, on):
        if on:
            hello = 1
        else:
            self.loseTimer = time.time()
        self.lose()
        
    def land(self):
        self.state='stop'
        print("Score =",self.score)

    def updatePoints(self, list):
        points = sum(list)
        print(points)

    def win(self):
        print("YOU WIN")
        self.state='over'

    def lose(self):
        if (time.time() - self.loseTimer >= 5):
            print("YOU LOSE")
            self.state='over'
            