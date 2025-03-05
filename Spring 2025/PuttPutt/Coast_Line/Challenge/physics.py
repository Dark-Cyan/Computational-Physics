from vectors import*
import pop
import random

#Physics engine

##Switches - Booleans##
run = False

# Constants
HOLE=Vec(0,5,0)


t=0
dt=0.001

# Forces

FRIC=0.025

def friction(a):
    try: 
        return -1*a.vel.norm()*FRIC
    except ValueError:
        return Vec(0, 0, 0)


def forces(a):
    return friction(a)

def stop(a):
    global run
    #sink
    if (a.pos-HOLE).mag() < (0.054-0.032*a.vel.mag()):
        a.visible=False
        run = False
  
    
    elif a.pos.y>5.25:
        run = False
        a.visible=False
        
    elif a.vel.mag()<0.001:
        a.vel=Vec(0,0,0)
        run = False

def move(a,n):
    global run
    for i in range(n):
        if run:
            a.acc=forces(a)/a.m
            a.vel+=a.acc*dt
            a.pos+=a.vel*dt
            stop(a)