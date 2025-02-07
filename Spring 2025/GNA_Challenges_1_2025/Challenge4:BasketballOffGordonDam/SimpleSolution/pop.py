#create projectile populations
from vectors import *
import random

class Ball:

    def __init__(self, angle, speed, backspin):
        self.goal = 82
        self.r = 0.119
        self.m = 0.624
        self.C = 0.45
        self.mC=1.5e-2
        self.speed = speed
        self.backspin = backspin
        self.w=Vec(0,0,backspin)
        self.vel=Vec(speed*math.cos(math.radians(angle)),speed*math.sin(math.radians(angle)),0)
        self.pos=Vec(0,123,0)
        self.acc=Vec(0,0,0)
        self.range=0
        self.distance = abs(self.goal - self.range)
        self.angle = angle

launcher = []
lander = []

repeats = 200
for i in range(repeats):
    ball = Ball(0, 0, random.uniform(0, 20))
    launcher.append(ball)