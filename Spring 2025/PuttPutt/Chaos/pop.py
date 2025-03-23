# Where stuff is made

from vectors import*
import random


class Ball:

    def __init__(self,velocity,color):

        #Physics Variables
        self.pos = Vec(0,0,0)
        self.vel = velocity
        self.ivel=velocity
        self.r = 0.021335
        self.m = 0.045
        self.acc = None

        #Genetic Algorithm Variables
        self.score=0
        self.distance = 1000
        self.bounce=0

        #Graphics Variables
        self.color = color
        self.visible=True

        #Misc
        self.run = True
    
    def __repr__(self):

        return f"Ball - Vx: {self.ivel.x}, Vy: {self.ivel.y}"

class Family:

    def __init__(self, children, parent, standardDeviation):

        self.familyMembers = []
        self.familyMembers.append(parent)
        self.size = children + 1
        self.standardDeviation = standardDeviation
        for i in range(children):
            ball = Ball(Vec(random.gauss(parent.ivel.x, standardDeviation), random.gauss(parent.ivel.y, standardDeviation), 0), parent.color)
            self.familyMembers.append(ball)

#Population Variables
families = 10
children = 10
population = []
finished = 0

for i in range(families):
    ball=Ball(Vec(random.uniform(-5, 5),random.uniform(0.5, 5), 0), (random.randrange(0,255,1), random.randrange(0,255,1), random.randrange(0,255,1)))
    family = Family(children, ball, 5)
    population.append(family)