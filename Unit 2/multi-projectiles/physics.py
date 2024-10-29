#physics engine

from stuff import*

#environmentals

g=Vec(0,-9.8,0) #gravity N/kg

p=1.2 #air density
s = 3.5 * 10 ** -5
dt=0.001

#ball parameters

mass = 0.045
radius = 0.021335

#launch parameters

angle = 12
spin = -240 #negative for backspin positive for topspin
speed = 77
height = 0

#average

startAngle = 0
endAngle = 360
da = 90

balls = []
for i in range(startAngle,endAngle,da):
    baseball=Ball(mass,radius,Vec(0,height,0),speed,12,spin,12,i)
    balls.append(baseball)

ranges = []

run = True
go = False

def weight(a):
    return a.m*g

def airpseed(a):
    return a.vec - a.wind

def drag(a):
    return -0.5*a.C*a.A*p*abs(airpseed(a))*airpseed(a)

def netforce(a):
    return weight(a)+drag(a)+lift(a)

def lift(a):
    return s * (a.w.cross(airpseed(a)))

def move(a,reps):
    if go == True:
        for i in range(reps):
            acc=netforce(a)/a.m
            a.vec+=acc*dt
            a.pos+=a.vec*dt
            a.t+=dt
            checker(a)
            if run == False:
                break

def checker(a):
    global run
    global ranges

    #if abs(a.vec.y)<0.01:
    #    print(f'Max Height = {round(a.pos.y,2)} m')
    if a.pos.y > a.maxHeight:
        a.maxHeight = a.pos.y
        a.maxHeightTime = a.t
    if a.pos.y<0 and a.IDLE == False: #float and it's checking to see if you've hit the ground
        print(f'Time = {a.t} s')
        print(f'Range = {a.pos.x} m')
        #print(f'Range = {a.pos.x * 1.09361} yd')
        print(f'Final Speed = {a.vec.mag()} m/s')
        print(f'Max Height = {a.maxHeight} m')
        print(f'Max Height Time = {a.maxHeightTime} s')
        ranges.append(a.pos.x)
        a.IDLE = True