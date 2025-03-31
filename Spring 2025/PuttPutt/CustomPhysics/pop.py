# Where stuff is made

from vectors import*


class Ball:

    def __init__(self,velocity):

        self.newPos = Vec(2.8,-0.8,0)
        self.oldPos = Vec(2.8,-0.8,0)
        self.acceleration = Vec(0,0,0)

        self.vel = velocity
        self.ivel=velocity
        self.r = 0.021335
        self.m = 0.045
        self.acc = None
        self.visible=True
        self.bounce=0

    def updatePosition(self, dt):
        vel = self.newPos - self.oldPos
        self.oldPos = self.newPos
        self.newPos = self.newPos + vel + self.acceleration * dt * dt
        self.acc = "hi"

    def accelerate(self, acc):
        self.acceleration += acc

ball = Ball(Vec(-6,7,0))
