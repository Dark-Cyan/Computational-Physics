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

        self.maxSpeed = self.vec.mag()
        self.minSpeed = self.vec.mag()

        #self.recpos = queue.Queue(0)
        #self.recpos.put(self.pos)
        self.color = color
        self.name = name
        self.orbit = "Undefined"
        self.maxDistance = self.pos.mag()
        self.minDistance = self.pos.mag()

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

mass = (7.3e22, 5.4)
radius = (100, 50)

velocity = (Vec(0,0,0), Vec(2370, 0, 0))

startX = (0,0)
startY = (0,1737.5e3+5300)
startZ = (0,0)
start = (Vec(startX[0], startY[0], startZ[0]), Vec(startX[1], startY[1], startZ[1]))

color = ((246, 241, 213), (192, 192, 192))

name = ("Moon", "Cannonball")

for i in range(len(mass)):
    planet = celestialBody(mass[i],radius[i],start[i], velocity[i], color[i], name[i])
