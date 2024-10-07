#physics engine

from stuff import*

#environmentals

g=Vec(0,-9.8,0) #gracity N/kg
p=1.225 #air density
dt=0.01
t=0

#launch parameters

speed = 30
angle = 45

baseball=Ball(0.145,0.037,Vec(0,0,0),speed,angle)
print(baseball.vec)

run = True

def weight(a):
    return a.m*g

def drag(a):
    return -0.5*a.C*a.A*p*abs(a.vec)*a.vec

def move(a):

    force=weight(a)+drag(a)
    acc=force/a.m
    a.vec+=acc*dt
    a.pos+=a.vec*dt
    checker(a)

def checker(a):
    global run
    if a.pos.y<0: #float and it's checking to see if you've hit the ground
        print(a.pos.x)
        run = False

print(weight(baseball))
print(drag(baseball))