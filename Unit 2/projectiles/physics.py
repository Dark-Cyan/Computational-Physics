#physics engine

from stuff import*

#environmentals

g=Vec(0,-9.8,0) #gracity N/kg
p=1.2 #air density
dt=0.001
t=0

maxHeight = 0

#launch parameters

speed = 20
angle = 45
height = 0

baseball=Ball(4,0.10,Vec(0,height,0),speed,angle)

run = True
go = False

def weight(a):
    return a.m*g

def drag(a):
    return -0.5*a.C*a.A*p*abs(a.vec)*a.vec

def netforce(a):
    return weight(a)+drag(a)

def move(a,reps):
    global t
    if go == True:
        for i in range(reps):
            acc=netforce(a)/a.m
            a.vec+=acc*dt
            a.pos+=a.vec*dt
            t+=dt
            checker(a)

def checker(a):
    global run
    global maxHeight

    if abs(a.vec.y)<0.01:
        print(f'Max Height = {round(a.pos.y,2)} m')
    #if a.pos.y > maxHeight:
    #    maxHeight = a.pos.y
    if a.pos.y<0: #float and it's checking to see if you've hit the ground
        print(f'Time = {t} s')
        print(f'Range = {a.pos.x} m')
        print(f'Final Speed = {a.vec.mag()} m/s')
        #print(f'Max Height = {maxHeight} m')
        run = False