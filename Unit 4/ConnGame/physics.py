# physics.py

from vectors import*
from stuff import Lander

#constants intial stuff

g = Vec(0,-1.62,0)
t=0
dt=0.01

h = 200

lander=Lander(h)

def weight():
    return lander.m*g

def thrust():
    thrust=Vec(0,0,0)
    if lander.thrust_up:
        thrust+=Vec(0,2000,0)
    if lander.thrust_left:
        thrust+=Vec(-600,0,0)
    if lander.thrust_right:
        thrust+=Vec(600,0,0)
    return thrust

def forces():
    lander.force=weight()+thrust()

def move():
    forces()
    lander.acc=lander.force/lander.m
    lander.vel+=lander.acc*dt
    lander.pos+=lander.vel*dt