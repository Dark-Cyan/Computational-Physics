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
        a.pos = HOLE
        a.vel = Vec(0,0,0)
        a.visible=False
        a.run = False
        a.distance = 0
        pop.finished += 1
        a.score = a.speed
        return True
    
    elif a.pos.y>5.25:
        a.run = False
        a.visible=False
        a.distance = 1000
        a.vel = Vec(0,0,0)
        pop.finished += 1
        a.score = a.distance + a.speed
        return True
        
    elif a.vel.mag()<0.001:
        a.vel=Vec(0,0,0)
        a.run = False
        pop.finished += 1
        a.distance = abs(a.pos - HOLE)
        a.score = a.distance + a.speed
        return True

def move(a,n):
    if run and a.run:
        for i in range(n):
            a.acc=forces(a)/a.m
            a.vel+=a.acc*dt
            a.pos+=a.vel*dt
            if (stop(a)):
                break