from vectors import*
import math
import pop

#Environmentals

g=Vec(0,-9.8,0) #Newtons/kilogram - this force per unit mass
p= 1.2
t = 0
dt = 0.01
wind = Vec(0,0,0)

#forces

def weight(a):
    return a.m*g

def drag(a):
    return -0.5*p*a.C*math.pi*(a.r**2)*a.vel*a.vel.mag() #1/2CApv^2

def magnus(a):
    return a.mC*a.w