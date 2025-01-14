#game_logic.py

class Game:

    def __init__(self):
        self.state='play'
        self.score=0
        self.lives=3

    def crash(self):

        self.state='stop'
        self.lives-=1
        print("CRASH")
        print("Lives",self.lives)
        print("Score =",self.score)

    def land(self):
        self.state='stop'
        self.score+=1
        print("LAND")
        print("Lives",self.lives)
        print("Score =",self.score)

    def win(self):
        if self.score==3:
            print("YOU WIN")
            self.state='over'

    def lose(self):
        if self.lives==0:
            print("YOU LOSE")
            self.state='over'