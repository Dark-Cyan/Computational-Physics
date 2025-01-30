from vectors import*
import math
import pop
import genetics

#Environmentals

g=Vec(0,-1.62,0) #Newtons/kilogram - this force per unit mass
p= 0
t = 0
dt = 0.005
wind = Vec(0,0,0)

#forces

def weight(a):
    return a.m*g

def airspeed(a):
    return a.vel-wind

def forces(a):
    return weight(a)

#hitting the ground

def ground(a):
    if (a.pos.y<0 and a.pos.x <= 100) or (a.pos.y< (a.pos.x - 100) * math.tan(math.radians(25)) and a.pos.x > 100):
        a.range=a.pos.x
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