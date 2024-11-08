#the celestial bodies
import math
import queue
from vectors import*

planets = []

class celestialBody:

    def __init__(self,mass,radius,initial_pos,force,velocity,color):
        self.m=mass
        self.r=radius
        self.pos=initial_pos
        self.f = force
        self.vec = velocity
        self.recpos = queue.Queue(0)
        self.recpos.put(self.pos)
        self.color = color
        planets.append(self)

mass = (1e10, 1e16)
radius = (100, 100)

force = ((0,0,0), (0,0,0))
velocity = (Vec(20,-40,0), Vec(0,0,0))

startX = (-100, 50)
startY = (0, 0)
start = (Vec(startX[0], startY[0], 0), Vec(startX[1], startY[1], 0))

color = ((255,0,0), (0,0,255))

for i in range(len(mass)):
    planet = celestialBody(mass[i],radius[i],start[i], force[i], velocity[i], color[i])
