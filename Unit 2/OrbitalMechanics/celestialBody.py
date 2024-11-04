#the celestial bodies
import math
from vectors import*

class celestialBody:

    def __init__(self,mass,radius,initial_pos,speed,angle_deg):
        self.m=mass
        self.r=radius
        self.pos=initial_pos
        self.vec = Vec(math.cos(math.radians(angle_deg))*speed,math.sin(math.radians(angle_deg))*speed,0)


