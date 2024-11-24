#the celestial bodies
import math
import queue
from vectors import*

planets = []

class celestialBody:

    def __init__(self,mass,radius,initial_pos,velocity,color,name):
        self.m=mass
        self.r=radius
        self.pos=initial_pos
        self.startPoint=initial_pos
        self.distanceFromStart = 0
        self.vec = velocity
        self.recpos = queue.Queue(0)
        self.recpos.put(self.pos)
        self.color = color
        self.name = name
        self.orbit = "Undefined"
        self.maxDistance = self.pos.mag()
        self.minDistance = self.pos.mag()
        self.maxForce = 0

        #very unnecessary
        self.initAngle = 0
        self.angle = 0
        self.correctAngle()
        self.initAngle = self.angle
        self.correctAngle()

        planets.append(self)

    def correctAngle(planet):
        if planet.pos.y>= 0:
            radians = math.atan2(planet.pos.y,planet.pos.x)
        else:
            radians = math.pi * 2 + math.atan2(planet.pos.y,planet.pos.x)
        degrees = math.degrees(radians)
        planet.angle = (degrees - planet.initAngle + 360)%360 + 1

mass = (2.187251E30, 1.590728E30, 5.97E24)
radius = (100, 100, 100)

velocity = (Vec(0, 12938.27, 0), Vec(0, -17786, 0), Vec(0, -33297, 0))

startX = (-3.14902E10, 4.32998E10, 2.15639E11)
startY = (0,0,0)
startZ = (0,0,0)
start = (Vec(startX[0], startY[0], startZ[0]), Vec(startX[1], startY[1], startZ[1]), Vec(startX[2], startY[2], startZ[2]))

color = ((253, 184, 19), (252, 150, 1), (255, 228, 132))

name = ("Tatoo I", "Tatoo II", "Tatooine")

for i in range(len(mass)):
    planet = celestialBody(mass[i],radius[i],start[i], velocity[i], color[i], name[i])
