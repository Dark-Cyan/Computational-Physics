# Where stuff is made

from vectors import*
import random

class Ball:

    def __init__(self,velocity):

        self.pos = Vec(0,0,0)
        self.vel = velocity
        self.r = 0.021335
        self.m = 0.045
        self.acc = None
        self.visible=True

ball=Ball(Vec(0.05,2.45,0))