#the celestial bodies
import math
from vectors import*

class celestialBody:

    def __init__(self,mass,radius,initial_pos,force,velocity,color):
        self.m=mass
        self.r=radius
        self.pos=initial_pos
        self.f = force
        self.vec = velocity
        self.color = color


