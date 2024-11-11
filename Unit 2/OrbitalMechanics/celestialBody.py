#the celestial bodies
import math
import queue
from vectors import*

planets = []

class celestialBody:

    def __init__(self,mass,radius,initial_pos,velocity,color):
        self.m=mass
        self.r=radius
        self.pos=initial_pos
        self.vec = velocity
        self.recpos = queue.Queue(0)
        self.recpos.put(self.pos)
        self.color = color
        planets.append(self)

mass = (5.97219E24, 1988410E24)
radius = (100, 100)

velocity = (Vec(-2.721938833676917E+04, 1.301001220575709E+04, 2.722342885856932E-01), Vec(1.210213161761593E+1,-7.108630163798801,-1.931983570112581E-01))

startX = (6.412312668699121E+10, -8.954314476268431E+08)
startY = (1.318457264231664E+11, -7.136648792848191E+08)
startZ = (1.963735964163393E+07, 2.747324307441281E+07)
start = (Vec(startX[0], startY[0], startZ[0]), Vec(startX[1], startY[1], startZ[1]))

color = ((0,255,0), (100,30,0))

for i in range(len(mass)):
    planet = celestialBody(mass[i],radius[i],start[i], velocity[i], color[i])
