#stuff.py
from vectors import*

class Lander:
    def __init__(self):
        self.m=600
        self.pos=Vec(0,200,0)
        self.vel=Vec(0,0,0)
        self.acc=Vec(0,0,0)
        self.force=Vec(0,0,0)
        self.thrust_up=False
        self.thrust_left=False
        self.thrust_right=False

    def reset(self):

        self.pos=Vec(0,200,0)
        self.vel=Vec(0,0,0)
        self.acc=Vec(0,0,0)
        self.force=Vec(0,0,0)
        self.thrust_up=False
        self.thrust_left=False
        self.thrust_right=False
        