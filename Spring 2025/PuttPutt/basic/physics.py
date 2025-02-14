from vectors import*
import pop

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
        a.distance = 0
        pop.winners.append(a)
        pop.population.remove(a)
        #gen.next_gen()
        return True
    return False

def stop(a):
    if not sink(a) and a.vel.mag()<0.001:
        a.distance = abs(HOLE - a.pos)
        pop.losers.append(a)
        pop.population.remove(a)
        #gen.next_gen()
        return True
    
    return False

def move(a,n):
    if run:
        for i in range(n):
            a.acc=forces(a)/a.m
            a.vel+=a.acc*dt
            a.pos+=a.vel*dt
            if (sink(a)):
                break
            if (stop(a)):
                break