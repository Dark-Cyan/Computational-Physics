#create projectile populations
from vectors import *
import random

class Ball:

    def __init__(self, angle, speed, height):
        self.distance = 100000
        self.maxHeight = 0
        self.r = 0.08
        self.m = 15
        self.mC=3e-5
        self.speed = speed
        self.vel=Vec(speed*math.cos(math.radians(angle)),speed*math.sin(math.radians(angle)),0)
        self.pos=Vec(1000,height,0)
        self.acc=Vec(0,0,0)
        self.range = 100000 - self.maxHeight
        self.angle = angle
        if height > 25000:
            self.T = -131.21 + 0.00299 * height
            self.P = 2.488 * ((self.T + 273.1)/216.6)**-11.388
        elif height > 11000 and height < 25000:
            self.T = -56.46
            self.P = 22.65 * math.e * (1.73 - 0.000157 * height)
        else:
            self.T = 15.04 - 0.00649 * height
            self.P = 101.29 * ((self.T+273.1)/288.08)**5.256
        self.C = 0.5
        self.p = self.P / (0.2869 * (self.T+273.1))
        self.dt = 0.0001
        
        

launcher = []
lander = []

repeats = 199
for i in range(repeats):
    ball = Ball(90, random.uniform(1000, 41000), 8848.86)
    launcher.append(ball)