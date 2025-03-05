from vectors import*
import pop
import random

#Physics engine

##Switches - Booleans##
run = False

# Course Constants

#Hole 

HOLE=Vec(-2,1.5,0)

# Wall

WALL_B= Vec(-0.5,-5,0)
WALL_T=Vec(-0.5,1.5,0)
WALL_length=(WALL_B-WALL_T).mag()

#Valley

Valley=Vec(0.5,3,0)
Valley_r=1.5
slope=0.6
POND=Vec(0.5,3,0)
POND_r=0.5
   
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
    return friction(a) + sling(a)

def stop(a):

    dist_pond = (a.pos - Valley).mag()
    dist_hole = (a.pos - HOLE).mag()
    vmag = a.vel.mag()

    if dist_pond < POND_r:
        a.visible=False
        a.run = False
        a.distance = 1000
        pop.finished += 1
        return True
    
    elif dist_hole < (0.054 - 0.032 * vmag):
        a.pos = HOLE
        a.visible=False
        a.run = False
        a.distance = 0
        pop.finished += 1
        return True


    elif vmag < 0.01:
        a.vel=Vec(0,0,0)
        a.run = False
        pop.finished += 1
        a.distance = abs(HOLE - a.pos)
        return True
    
    return False


def detect_wall(a):

    d = (a.pos - WALL_T).mag() + (a.pos - WALL_B).mag()
    if d < WALL_length + 0.05:

        if a.vel.x < 0 and -0.5 < a.pos.x < -0.45:
            a.bounce -= 10
            a.pos -= a.vel * dt
            a.vel.x *= -1
        elif a.vel.x > 0 and -0.55 < a.pos.x < -0.5:
            a.bounce -= 10
            a.pos -= a.vel * dt
            a.vel.x *= -1


def sling(a):

    dv = a.pos - Valley
    dvmag = dv.mag()
    return -slope * dv.norm() / dvmag if dvmag < Valley_r else Vec(0, 0, 0)
        

def move(a,n):
    if run and a.run:
        for i in range(n):
            a.acc=forces(a)/a.m
            a.vel+=a.acc*dt
            a.pos+=a.vel*dt
            detect_wall(a)
            if (stop(a)):
                break