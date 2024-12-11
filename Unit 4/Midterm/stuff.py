from vectors import*

class stuff:
    def __init__(self, mass, radius, position, gravity, anchor):
        self.m = mass
        self.r = radius
        self.pos = position
        self.vel = Vec(0,0,0)
        self.acc = Vec(0,0,0)
        self.force = Vec(0,0,0)
        self.grav = gravity
        self.anchor = anchor
        fruits.append(self)

fruits = []

