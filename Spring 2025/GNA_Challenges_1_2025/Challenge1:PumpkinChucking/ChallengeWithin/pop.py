#create projectile populations
from vectors import *
import random

class Ball:

    def __init__(self, angle, speed, backspin, length, windAngle):
        self.length = 30.48
        self.goal = 200
        self.r = 0.125
        self.m = 4.2
        self.C = 0.3
        self.mC=3e-5
        self.speed = speed
        self.w=Vec(0,0,backspin)
        self.vel=Vec(speed*math.cos(math.radians(angle)),speed*math.sin(math.radians(angle)),0)
        self.pos=Vec(0,math.sin(math.radians(angle)) * length,0)
        self.acc=Vec(0,0,0)
        self.range=0
        self.distance = abs(self.goal - self.range)
        self.angle = angle
        self.wind = Vec(13.5*math.cos(math.radians(windAngle)), 13.5*math.sin(math.radians(windAngle)),0)
        self.windAngle = windAngle

launcher = []
lander = []

repeats = 200
for i in range(repeats):
    ball = Ball(35, 330, 0, 30.48, random.uniform(0,90))
    launcher.append(ball)