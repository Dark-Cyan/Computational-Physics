#create projectile populations
from vectors import *
import random

class Ball:

    def __init__(self, angle):
        self.r = 0.021335
        self.m = 0.045
        self.mC=3e-5
        self.speed = 12/math.sin(math.radians(angle/3 + 35))
        self.w=Vec(0,0,0)
        self.vel=Vec(self.speed*math.cos(math.radians(angle)),self.speed*math.sin(math.radians(angle)),0)
        self.pos=Vec(0,0,0)
        self.acc=Vec(0,0,0)
        self.range=0
        self.angle = angle
        self.impact = 0

launcher = []
lander = []

repeats = 200
for i in range(repeats):
    ball = Ball(random.uniform(0,100))
    launcher.append(ball)