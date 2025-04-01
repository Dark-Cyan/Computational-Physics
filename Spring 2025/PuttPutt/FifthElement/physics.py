from vectors import*
import random
import math

run = False

#Constants
dt = 0.004
FRIC=0.025

#Clutter Constants
circleBumperPos = Vec(0, 4, 0)
circleBumperRad = 0.5

def forces(a):
    
    return friction(a) + pinball_slope(a)

def friction(a):
    try: 
        return -1*a.velocity.norm()*FRIC
    except ValueError:
        
        return Vec(0, 0, 0)
    
def pinball_slope(a):
    return Vec(0,-0.1,0)

def edges(a):
    if a.position.x > 2.9 - a.radius or a.position.x < -2.4 + a.radius:
        a.velocity.x *= -1
    if a.position.y > 7.9 - a.radius or a.position.y < 0.1 + a.radius:
        a.velocity.y *= -1

def collision(a):
    #Circle Bumper 
    if abs(a.position - circleBumperPos) < a.radius + circleBumperRad:
        bounceDirection = (a.position - circleBumperPos).norm()
        a.velocity = abs(a.velocity) * bounceDirection
    
    if abs(a.position - Vec(0.25, 5.25, 0)) > 2.65 - a.radius and a.position.y >= 5.25:
        #NEED TO FIX
        bounceDirection = (Vec(0.25, 5.25, 0) - a.position).norm()
        a.velocity = abs(a.velocity) * bounceDirection

    if a.position.x < 0 and a.position.y  - a.radius <= 0.1 - 5/24 * a.position.x:
        wallAngle = math.atan2(5, 24) 
        incidenceAngle = math.atan2(a.velocity.y, a.velocity.x)
        reflectionAngle =  (2 * wallAngle) - incidenceAngle
        a.velocity.x *= math.cos(reflectionAngle)
        a.velocity.y *= math.sin(reflectionAngle)

    if a.position.x > 0 and a.position.y  - a.radius <= 0.1 + 5/24 * a.position.x:
        wallAngle = math.atan2(-5, 24) 
        incidenceAngle = math.atan2(a.velocity.y, a.velocity.x)
        reflectionAngle =  (2 * wallAngle) - incidenceAngle
        a.velocity.x *= math.cos(reflectionAngle)
        a.velocity.y *= math.sin(reflectionAngle)

def move(a,n):
    for i in range(n):
        if run:
            #a.acceleration=forces(a)/a.mass
            a.velocity+=a.acceleration*dt
            a.position+=a.velocity*dt
            edges(a)
            collision(a)