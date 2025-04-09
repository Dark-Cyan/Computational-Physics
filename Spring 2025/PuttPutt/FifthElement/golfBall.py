from vectors import Vec
import random

class Ball:
    def __init__(self, velocity, color):
        #Positional Variables
        self.position = Vec(2.75, 0.25, 0)
        self.velocity = velocity
        self.initialVelocity = velocity
        self.acceleration = Vec(0, 0, 0)
        
        #Matter Variables
        self.radius = 0.021335
        self.mass = 0.045

        #Graphical Variables
        self.color = color
        self.visible = True

        self.run = True
        self.score=0
        population.append(self)

population = []
winners = []
losers = []
final = []
populationSize = 1 #100

# for i in range(populationSize):
#     ball=Ball(Vec(random.uniform(-3,3),random.uniform(5,15),0), (random.randrange(0,255,1), random.randrange(0,255,1), random.randrange(0,255,1)))

ball = Ball(Vec(3.909517465750703, 14.888680327361048, 0.0), (random.randrange(0,255,1), random.randrange(0,255,1), random.randrange(0,255,1)))
 