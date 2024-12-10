from vectors import*

g = Vec(0,-9.8,0)
t=0
dt=0.01

def weight(a):
    return a.m*g

def forces(a):
    a.force=weight(a)

def move(a, reps):
    for i in range(reps):
        forces()
        a.acc=a.force/a.m
        a.vel+=a.acc*dt
        a.pos+=a.vel*dt