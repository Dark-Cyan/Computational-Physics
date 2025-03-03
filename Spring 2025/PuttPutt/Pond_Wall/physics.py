from vectors import*
import pop
import random

#Physics engine

##Switches - Booleans##
run = False

# Constants
HOLE=Vec(0,5,0)
POND=Vec(-3.75,3,0)
POND_r=4
WALLLB=Vec(0.5,7,0)
WALLLT=Vec(3,7,0)
WALLRB=Vec(3,4.5,0)
WALLRT=Vec(3,7,0)
WALLnorm = (WALLRB-WALLLB).cross(Vec(0,0,1)).norm()

spray=0.5
cor=0.7
cor_range=0.02
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

def stop(a):
    #sink
    if (a.pos-HOLE).mag() < (0.054-0.032*a.vel.mag()):
        a.pos=HOLE
        a.run = False
        pop.finished += 1
        a.distance = 0
        return True
    
    elif (a.pos-POND).mag()<POND_r:
        a.vel=Vec(0,0,0)
        a.distance = 1000
        a.run = False
        pop.finished += 1
        a.distance = 1000
        return True
    
    elif a.vel.mag()<0.001:
        a.vel=Vec(0,0,0)
        a.run = False
        pop.finished += 1
        a.distance = abs(HOLE - a.pos)
        return True

    return False

def collision(a):
    a.pos-=a.vel*dt
    cWALLnorm=WALLnorm.rot2D(random.gauss(0,spray))
    speedloss=random.uniform(cor-cor_range,cor+cor_range)
    Pspeed=a.vel.dot(cWALLnorm)
    bounce=2*speedloss*Pspeed*cWALLnorm
    a.vel-=bounce

def detect(a):
    d=(a.pos-WALLLB).mag()+(a.pos-WALLRB).mag()
    if d < (WALLLB-WALLRB).mag()+0.05:
        eff_y=-1*a.pos.x+7.5
        if a.pos.y>eff_y:
            collision(a)


def move(a,n):
    for i in range(n):
        if run and a.run:
            a.acc=forces(a)/a.m
            a.vel+=a.acc*dt
            a.pos+=a.vel*dt
            detect(a)
            if (stop(a)):
                break