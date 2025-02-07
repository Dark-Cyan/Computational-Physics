#create projectile populations
from vectors import *
import random

class Ball:

    def __init__(self, angle):
        self.goal = 160
        self.r = 0.021335
        self.m = 0.045
        self.C = 0.2
        self.mC=3e-5
        self.speed = 45
        self.w=Vec(0,0,250)
        self.vel=Vec(self.speed*math.cos(math.radians(angle)),self.speed*math.sin(math.radians(angle)),0)
        self.pos=Vec(0,8,0)
        self.acc=Vec(0,0,0)
        self.range=0
        self.distance = abs(self.goal - self.range)
        self.angle = angle

launcher = []
lander = []

repeats = 200
for i in range(repeats):
    ball = Ball(random.uniform(-90,90))
    launcher.append(ball)