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

mass = (1988410E24, 2.2E14)
radius = (100, 111)

velocity = (Vec(1.210213161761593E+01, -7.108630163798801, 1.931983570112581E-01), Vec(8.024309821151976E+02, 4.310680197152988E+02, 1.484144220678963E+02))

startX = (-8.954314476268431E+08, -2.947065953655099E+12)
startY = (-7.136648792848191E+08, 4.089719790890038E+12)
startZ = (2.747324307441281E+07, -1.485070694438470E+12)
start = (Vec(startX[0], startY[0], startZ[0]), Vec(startX[1], startY[1], startZ[1]))

color = ((249,215,28), (255, 0, 0))

name = ("Sun", "Unknown")

for i in range(len(mass)):
    planet = celestialBody(mass[i],radius[i],start[i], velocity[i], color[i], name[i])
