#create projectile populations
from vectors import *
import random

class Ball:

    def __init__(self, angle, speed, backspin, height):
        self.r = 0.021335
        self.m = 0.045
        self.C = 0.3
        self.mC=3.5e-5
        self.w=Vec(0,0,backspin)
        self.vel=Vec(speed*math.cos(math.radians(angle)),speed*math.sin(math.radians(angle)),0)
        self.pos=Vec(0,height,0)
        self.acc=Vec(0,0,0)
        self.range=0

launcher = []
lander = []

repeats = 100
for i in range(repeats):
    ball = Ball(random.uniform(0,90),42,0,0)
    launcher.append(ball)