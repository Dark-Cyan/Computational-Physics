#create projectile populations
from vectors import *
import random

class Ball:

    def __init__(self, angle, speed, height, fuel):
        self.distance = 100000
        self.maxHeight = 0
        self.r = 0.3
        self.m = 2000 + fuel
        self.startFuel = fuel
        self.fuel = fuel
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
        self.C = 0.35
        self.p = self.P / (0.2869 * (self.T+273.1))
        self.dt = 1
        
        

launcher = []
lander = []

repeats = 200
for i in range(repeats):
    ball = Ball(90, 0, 0, random.uniform(2000, 3000))#random.uniform(0,6163))
    launcher.append(ball)