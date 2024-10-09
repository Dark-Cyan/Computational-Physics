#physics engine

from stuff import*

#environmentals

g=Vec(0,-9.8,0) #gracity N/kg
p=1.2 #air density
dt=0.001
t=0

maxHeight = 0

#launch parameters

speed = 100
angle = 32.6

baseball=Ball(4,0.10,Vec(0,280,0),speed,angle)

run = True

def weight(a):
    return a.m*g

def drag(a):
    return -0.5*a.C*a.A*p*abs(a.vec)*a.vec

def netforce(a):
    return weight(a)+drag(a)

def move(a):
    global t
    acc=netforce(a)/a.m
    a.vec+=acc*dt
    a.pos+=a.vec*dt
    t+=dt
    checker(a)

def checker(a):
    global run
    global maxHeight
    if a.pos.y > maxHeight:
        maxHeight = a.pos.y
    if a.pos.y<0: #float and it's checking to see if you've hit the ground
        print(f'Time = {t} s')
        print(f'Range = {a.pos.x} m')
        print(f'Final Speed = {a.vec.mag()} m/s')
        print(f'Max Height = {maxHeight} m')
        run = False