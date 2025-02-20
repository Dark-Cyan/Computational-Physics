from vectors import*
import pop

#Physics engine

##Switches - Booleans##
run = False

# Constants
HOLE=Vec(0,5,0)
HILL=Vec(-0.3,1.5,0)
VALLEY=Vec(0.3,3.5,0)
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
    
def radial_force(a, center, outer, inner, direction):

    r = a.pos - center
    mag = r.mag()

    if 1 > mag > 0.5:
        return direction * (outer / mag) * r.norm()
    
    elif 0 < mag < 0.5:
        return direction * (inner * mag) * r.norm()
    
    else:
        return Vec(0,0,0)

def hill(a):
    return radial_force(a, HILL, 0.05, 0.2, 1)

def valley(a):
    return radial_force(a, VALLEY, 0.05, 0.2, -1)

def forces(a):
    return friction(a)+hill(a)+valley(a)

##___Stuff that can happen to ball___ ##

def stop(a):
    #sink
    if (a.pos-HOLE).mag() < (0.054-0.032*a.vel.mag()):
        a.pos=HOLE
        a.distance = 0
        pop.winners.append(a)
        pop.population.remove(a)
        return True
    elif a.vel.mag()<0.001:
        a.vel=Vec(0,0,0)
        a.distance = abs(HOLE - a.pos)
        pop.losers.append(a)
        pop.population.remove(a)
        return True

    return False



def move(a,n):
    if run:
        for i in range(n):
            a.acc=forces(a)/a.m
            a.vel+=a.acc*dt
            a.pos+=a.vel*dt
            if (stop(a)):
                break