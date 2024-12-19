from vectors import*

class stuff:
    def __init__(self, mass, radius, position, vel, gravity, anchor, color, type):
        self.m = mass
        self.r = radius
        self.pos = position
        self.vel = vel
        self.acc = Vec(0,0,0)
        self.force = Vec(0,0,0)
        self.grav = gravity
        self.anchor = anchor
        self.col = color
        self.type = type
        self.falling = False
        fruits.append(self)
        points.append(POINTS[type])

POINTS = [1,3,6,10,15,21,28,36,45,55,66]

fruits = []
points = []

