#create projectile populations
from vectors import *
import random

class Ball:

    def __init__(self, angle, speed, height):
        self.maxHeight = 0
        self.r = 0.08
        self.m = 15
        self.C = 0.5
        self.mC=3e-5
        self.speed = speed
        self.vel=Vec(speed*math.cos(math.radians(angle)),speed*math.sin(math.radians(angle)),0)
        self.pos=Vec(1000,height,0)
        self.acc=Vec(0,0,0)
        self.range = 100000 - self.maxHeight
        self.angle = angle

launcher = []
lander = []

repeats = 200
for i in range(repeats):
    ball = Ball(90, random.uniform(10,1000), 0)
    launcher.append(ball)