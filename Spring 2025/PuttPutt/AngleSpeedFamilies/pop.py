# Where stuff is made

from vectors import*
import random

class Ball:

    def __init__(self, angle, speed, color, familyNum):

        self.pos = Vec(0,0,0)
        self.distance = 1000
        self.speed = speed
        self.angle = angle
        self.vel = Vec(speed*math.cos(math.radians(angle)),speed*math.sin(math.radians(angle)),0)
        self.r = 0.021335
        self.m = 0.045
        self.acc = None
        self.color = color
        self.familyNum = familyNum
        self.run = True
        self.score=0
        self.bounce=0
        self.visible=True

class Family:

    def __init__(self, size, lBound, hBound, standardDeviation, familyNum):
        self.fn = familyNum
        self.size = int(size)
        self.familyMembers = []
        self.standardDeviation = standardDeviation
        self.color = (random.randrange(0,255,1), random.randrange(0,255,1), random.randrange(0,255,1))
        for i in range(self.size):
            ball=Ball(random.uniform(lBound, hBound), random.uniform(0.5,4.5), (self.color), familyNum)
            self.familyMembers.append(ball)
        self.average = None

populationSize, families = 200, 10
population = []
winners = []
losers = []
finished = 0
final = [] 

2.7

for i in range(0,180,int(180/families)):
    family = Family(populationSize/families,i,i+(180/families), 4, int(i/int(180/families)))
    population.append(family)
