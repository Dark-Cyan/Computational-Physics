from vectors import*
import math
import pop
import genetics

#Environmentals

g=Vec(0,-9.8,0) #Newtons/kilogram - this force per unit mass
#p= 1.15
t = 0
#dt = 0.01
wind = Vec(0,0,0)

#forces

def weight(a):
    return a.m*g

def airspeed(a):
    return a.vel-wind

def drag(a):
    return -0.5*a.p*a.C*math.pi*(a.r**2)*airspeed(a)*airspeed(a).mag() #1/2CApv^2

def thrust(a):
    if a.fuel >= 30 * a.dt:
        a.fuel -= 30 * a.dt
        a.m -= 30 * a.dt
        return Vec(0,80000,0)
    else:
        return Vec(0,0,0)

def forces(a):
    return weight(a) + drag(a) + thrust(a)

#hitting the ground

def ground(a):
    if a.pos.y<0:
        a.pos.y=0
        a.range=a.pos.x
        pop.lander.append(a)
        pop.launcher.remove(a)
        genetics.next_gen()

def update(a):
    # print(airspeed(a), -0.5*a.p*a.C*math.pi*(a.r**2), a.pos.y)
    # print(f"a.weight() = {weight(a)}, type: {type(weight(a))}")
    # print(f"a.drag() = {drag(a)}, type: {type(drag(a))}")
    # print(f"a.r = {thrust(a)}, type: {type(thrust(a))}")
    # print(f"a.r**2 = {a.r**2}, type: {type(a.r**2)}")
    a.acc = forces(a)/a.m #F = ma
    a.vel += a.acc * a.dt
    a.pos += a.vel * a.dt
    a.dt = 1/(abs(a.acc)+1)
    if (a.dt > 0.01):
        a.dt = 0.01
    fixModel(a)
    ground(a)

def fixModel(a):
    if a.pos.y > 25000:
        a.T = -131.21 + 0.00299 * a.pos.y
        a.P = 2.488 * ((a.T + 273.1)/216.6)**-11.388
    elif a.pos.y > 11000 and a.pos.y < 25000:
        a.T = -56.46
        a.P = 22.65 * math.e**(1.73 - 0.000157 * a.pos.y)
    elif a.pos.y < 11000:
        a.T = 15.04 - 0.00649 * a.pos.y
        a.P = 101.29 * ((a.T+273.1)/288.08)**5.256
    if (a.pos.y >= a.maxHeight):
        a.maxHeight = a.pos.y
        a.range = 100000 - a.pos.y
        a.distance = abs(100000 - a.maxHeight)
    a.p = a.P / (0.2869 * (a.T+273.1))

    # if (a.pos.y > a.maxHeight):
    #     a.maxHeight = a.pos.y
    # a.range = 100000 - a.pos.y
    # a.distance = 100000 - a.maxHeight
    #a.p = a.P / (0.2869 * (a.T+273.1))

def move(reps):
    global t
    for i in range(reps):
        t += 1
        for i in pop.launcher:
            update(i)