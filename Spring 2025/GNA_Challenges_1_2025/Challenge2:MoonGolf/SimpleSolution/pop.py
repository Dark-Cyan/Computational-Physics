#create projectile populations
from vectors import *
import random

class Ball:

    def __init__(self, angle, speed, backspin):
        self.r = 0.021335
        self.m = 0.045
        self.mC=3e-5
        self.speed = speed
        self.w=Vec(0,0,backspin)
        self.vel=Vec(speed*math.cos(math.radians(angle)),speed*math.sin(math.radians(angle)),0)
        self.pos=Vec(0,0,0)
        self.acc=Vec(0,0,0)
        self.range=0
        self.distance = abs(self.goal - self.range)
        self.angle = angle

launcher = []
lander = []

repeats = 200
for i in range(repeats):
    ball = Ball(random.uniform(0,100), 330, 0, 30.48)
    launcher.append(ball)