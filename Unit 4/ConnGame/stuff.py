#stuff.py
from vectors import*

class Lander:
    def __init__(self, h):
        self.m=600
        self.pos=Vec(0,h,0)
        self.vel=Vec(0,0,0)
        self.acc=Vec(0,0,0)
        self.force=Vec(0,0,0)
        self.thrust_up=False
        self.thrust_left=False
        self.thrust_right=False