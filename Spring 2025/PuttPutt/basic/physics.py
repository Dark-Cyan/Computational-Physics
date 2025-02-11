from vectors import*
import pop

#Physics engine

##Switches - Booleans##
#run = False

# Constants
HOLE=Vec(0,5,0)
t=0
dt=0.001

# Forces

FRIC=0.025

def friction(a):
    #We haven't seen this yet. It's very nice, basically if what's in the
    #'try block' runs without error, then that's it, and the compiler moves on
    #otherwise it checks for the exceptions :)
    try: 
        return -1*a.vel.norm()*FRIC
    except ValueError:
        return Vec(0, 0, 0)
    
def forces(a):
    return friction(a)

##___Stuff that can happen to ball___ ##

def sink(a):
    if (a.pos-HOLE).mag() < (0.054-0.032*a.vel.mag()):
        a.pos=HOLE
        a.run = False
        return True

    return False

def stop(a):
    if not sink(a) and a.vel.mag()<0.001:
        a.vel=Vec(0,0,0)
        a.run = False
        return True
    
    return False

def move(a,n):
    for i in range(n):
        if a.run:
            a.acc=forces(a)/a.m
            a.vel+=a.acc*dt
            a.pos+=a.vel*dt
            sink(a)
            stop(a)