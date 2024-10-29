#the stuff
import math
from vectors import*

class Ball:

    def __init__(self,mass,radius,initial_pos,speed,angle_deg,spin,windSpeed, windAngle):
        self.m=mass
        self.r=radius
        self.A=math.pi*radius**2
        self.C=0.3
        self.pos=initial_pos
        self.vec = Vec(math.cos(math.radians(angle_deg))*speed,math.sin(math.radians(angle_deg))*speed,0)
        self.w = Vec(0,0,-spin) #only works for 2D rn
        self.wind = Vec(math.cos(math.radians(windAngle))*windSpeed,0,math.sin(math.radians(windAngle))*windSpeed)
        self.IDLE = False
        self.maxHeight = 0
        self.maxHeightTime = 0
        self.t = 0


