#create projectile populations
from vectors import *
import random

class Ball:

    def fixSpeed(a):
        a.speed = 120/(a.backspin-20)+30
        a.vel = Vec(a.speed*math.cos(math.radians(a.angle)),a.speed*math.sin(math.radians(a.angle)),0)

    def __init__(self, angle, backspin):
        self.goal = 82
        self.r = 0.119
        self.m = 0.624
        self.C = 0.45
        self.mC=1.5e-2
        self.backspin = backspin
        if backspin >= 16:
            self.backspin = 16
        if backspin <= 0:
            self.backspin = 0
        self.speed = 120/(self.backspin-20)+30
        self.w=Vec(0,0,backspin)
        self.vel=Vec(self.speed*math.cos(math.radians(angle)),self.speed*math.sin(math.radians(angle)),0)
        self.pos=Vec(0,126,0)
        self.acc=Vec(0,0,0)
        self.range=0
        self.distance = abs(self.goal - self.range)
        self.angle = angle
        Ball.fixSpeed(self)

    




launcher = []
lander = []

repeats = 200
for i in range(repeats):
    ball = Ball(random.uniform(-90, 90), random.uniform(0,16))
    #print(ball.speed, ball.angle, ball.vel)
    launcher.append(ball)