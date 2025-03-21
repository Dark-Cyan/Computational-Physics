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
    dist_hole = (a.pos - HOLE).mag()
    #sink
    if (a.pos-HOLE).mag() < (0.054-0.032*a.vel.mag()):
        a.visible=False
        a.run = False
        pop.finished += 1
        a.distance = dist_hole
        a.score = abs(a.ivel)
    
    elif a.pos.y>5.25:
        a.run = False
        a.visible=False
        pop.finished += 1
        a.distance = 100000
        a.score = 1000 + abs(a.ivel)
        
    elif a.vel.mag()<0.001:
        a.vel=Vec(0,0,0)
        a.run = False
        pop.finished += 1
        a.distance = dist_hole
        a.score = dist_hole + abs(a.ivel)

    elif abs(a.pos.x) > 3:
        a.vel=Vec(0,0,0)
        a.run = False
        pop.finished += 1
        a.distance = dist_hole
        a.score = 1000 + abs(a.ivel)

def move(a,n):
    for i in range(n):
        if run and a.run:
            a.acc=forces(a)/a.m
            a.vel+=a.acc*dt
            a.pos+=a.vel*dt
            stop(a)