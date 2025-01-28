from vectors import*
import math
import pop
import genetics

#Environmentals

g=Vec(0,-9.8,0) #Newtons/kilogram - this force per unit mass
p= 0.97
t = 0
dt = 0.005
wind = Vec(14,1,0)

#forces

def weight(a):
    return a.m*g

def airspeed(a):
    return a.vel-wind

def forces(a):
    return weight(a)

#hitting the ground

def ground(a):
    if a.pos.y<0:
        a.pos.y=0
        a.range=a.pos.x
        a.distance = abs(a.goal - a.range)
        pop.lander.append(a)
        pop.launcher.remove(a)
        genetics.next_gen()

def update(a):
    a.acc = forces(a)/a.m #F = ma
    a.vel += a.acc * dt
    a.pos += a.vel * dt
    ground(a)

def move(reps):
    global t
    for i in range(reps):
        t += dt
        for i in pop.launcher:
            update(i)