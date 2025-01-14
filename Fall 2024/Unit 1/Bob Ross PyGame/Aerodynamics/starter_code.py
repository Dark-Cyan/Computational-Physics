#What follows is unstructured spaghetti code, however it also
#lays things out in as straightforward a manner as possible, meaning
#no steps are skipped.

import math

class Ball:

    def __init__(self,mass,radius,pos,vel,dragC):

        self.pos=pos
        self.mass=mass
        self.vel=vel
        self.acc=0
        self.C=dragC
        self.A=math.pi*radius**2


t=0
dt=0.01 #step - time interval between updates
g=9.8 #Newtons/kg on/ or near the Earth
p=1.15 #air density

faller=Ball(10,0.1,100,0,0.5) #mass of 10 kg, radius = 0.1m
#initial pos = 100, initial = vel, drag Coeff = 0.5

run = True

def move(a):
    global run
    drag=-0.5*a.C*a.A*p*a.vel*abs(a.vel)
    force=(-a.mass*g)+(drag)
    a.acc=(force)/a.mass
    a.pos+=a.vel*dt
    a.vel+=a.acc*dt
    t+=dt
    if a.pos<0:
        print(a.vel)
        a.vel=0
        run = False

while run == True:
    move(faller)
