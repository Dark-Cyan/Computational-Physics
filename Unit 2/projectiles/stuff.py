#the stuff
import math
from vectors import*

class Ball:

    def __init__(self,mass,radius,initial_pos,speed,angle_deg):
        self.m=mass
        self.r=radius
        self.A=math.pi*radius**2
        self.C=0.47
        self.pos=initial_pos
        self.vec = Vec(math.cos(math.radians(angle_deg))*speed,math.sin(math.radians(angle_deg))*speed,0)

