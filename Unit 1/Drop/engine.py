#physics engine

import ball
import math

#physics stuff

t=0
dt=0.01 #step - time interval between updates
g=9.8 #Newtons/kg on/ or near the Earth
p=1.15 #air density
tailwind = 57.7798318837963

faller=ball.Ball(1435,1.98,0,0,0.33) #mass of 10 kg, radius = 0.1m
#initial pos = 100, initial = vel, drag Coeff = 0.5

def fixModel(a):
    a.T = 15.04 - 0.00649 * a.pos
    a.P = 101.29 * ((a.T+273.1)/288.08)**5.256
    a.C = a.P / (0.2869 * (a.T + 273.1))

def move(a):
    global t
    global tailwind
    t = t + dt
    #fixModel(faller)
    airspeed = a.vel# - tailwind
    drag=-0.5*a.C*a.A*p*airspeed*abs(airspeed)
    #force=(-a.mass*g)+(drag)
    #force = 1.3 * 10**4 + drag
    force = 1.54 * 10**4 - 128 * a.vel + drag
    a.acc=(force)/a.mass
    a.pos+=a.vel*dt
    a.vel+=a.acc*dt
    #if a.pos<1000:
    #    a.A = math.pi*3**2
    #    a.C = 1.6
    if t >= 1000: #a.pos/1000/1.609>=1: #a.vel*2.23694>=124
        #print(a.vel*2.23694)
        print(a.vel*2.23694)
        a.vel=0
        return False
    return True