# Where stuff is made

from vectors import*


class Ball:

    def __init__(self,velocity):

        self.pos = Vec(2.8,-0.8,0)
        self.vel = velocity
        self.ivel=velocity
        self.r = 0.021335
        self.m = 0.045
        self.acc = None
        self.visible=True

ball = Ball(Vec(1,3,0))