# Where stuff is made

from vectors import*
import random

class Ball:

    def __init__(self,velocity, color):

        self.pos = Vec(0,0,0)
        self.distance = 1000
        self.speed = (velocity.x ** 2 + velocity.y ** 2) ** 0.5
        self.initVel = velocity
        self.vel = velocity
        self.r = 0.021335
        self.m = 0.045
        self.acc = None
        self.color = color
        population.append(self)

population = []
winners = []
losers = []
final = []
populationSize = 200

for i in range(populationSize):
    ball=Ball(Vec(random.uniform(-1,1),random.uniform(1.5,2.5),0), (random.randrange(0,255,1), random.randrange(0,255,1), random.randrange(0,255,1)))