from vectors import*
import pop
import random

#Physics engine

##Switches - Booleans##
run = False

# Course Constants

#HOLE

HOLE=Vec(0,5,0)

#HILLS
 
HILLS=[]
HILL_R=0.4

def odd_even_value(n):
    return 0 if n % 2 == 0 else 0.5

for i in range(-3,4,1):
    for j in range(1,6,1):
        HILL=Vec(i+odd_even_value(j),j+0.5,0)
        HILLS.append(HILL)

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

def hill_slope(a):

    hill_force = Vec(0, 0, 0)
    for hill in HILLS:
        direction = (a.pos - hill).norm()
        distance = (a.pos - hill).mag()
        if distance < HILL_R:
            if distance < HILL_R / 2:
                hill_force = 2.5*direction * distance
            else:
                hill_force = 0.1*direction * (1 / distance)

    return hill_force
        
def forces(a):
    
    return friction(a)+hill_slope(a)

def forces(a):

    return friction(a)+ hill_slope(a)

def stop(a):

    dist_hole = (a.pos - HOLE).mag()
    vmag = a.vel.mag()
    
    if dist_hole < (0.054 - 0.032 * vmag):
        a.pos = HOLE
        a.visible=False
        a.run = False
        a.distance = 0
        pop.finished += 1
        a.score = a.speed
        return True
 
    elif vmag < 0.01 and a.acc.mag()<0.6:
        a.vel=Vec(0,0,0)
        a.run = False
        pop.finished += 1
        a.distance = dist_hole
        a.score = a.distance# + a.speed
        return True
    
    elif abs(a.pos.x) > 3 or a.pos.y < -1 or a.pos.y > 7:
        a.run = False
        pop.finished += 1
        a.distance = dist_hole
        a.score = dist_hole + a.speed + abs(a.vel) * 3
        a.vel=Vec(0,0,0)
        return True


def move(a,n):
    for i in range(n):
        if run and a.run:
            a.acc=forces(a)/a.m
            a.vel+=a.acc*dt
            a.pos+=a.vel*dt
            if (stop(a)):
                break