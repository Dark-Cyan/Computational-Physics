from vectors import*
import random
import math

run = False

#Constants
dt = 0.01
FRIC=0.025

#Clutter Constants
circleBumperPos = Vec(0, 4, 0)
circleBumperRad = 0.5

HOLE=Vec(0,0.15,0)

def forces(a):
    
    return friction(a) + pinball_slope(a)

def friction(a):
    try: 
        #return -1*a.velocity.norm()*FRIC
        return -1*Vec(0, a.velocity.y, 0).norm()*FRIC
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
        #a.velocity = abs(a.velocity) * bounceDirection
        a.velocity = 5.00 * bounceDirection
    
    if abs(a.position - Vec(0.25, 5.25, 0)) > 2.65 - a.radius and a.position.y >= 5.25:
        bounceDirection = (Vec(0.25, 5.25, 0) - a.position).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(bounceDirection)) * bounceDirection

    if a.position.x <= 0 and a.position.y  - a.radius <= 0.1 - 5/24 * a.position.x:
        wallAngle = Vec(5,24,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle
        a.position.y = 0.1 - 5/24 * a.position.x + a.radius

    if a.position.x > 0 and a.position.x <= 2.5 and a.position.y  - a.radius <= 0.1 + 5/24 * a.position.x:
        wallAngle = Vec(-5,24,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle
        a.position.y = 0.1 + 5/24 * a.position.x + a.radius

    if a.position.x >= 2.4 and a.position.x <= 2.5 and a.position.y <= 6 and a.position.y >= 0:
        a.velocity.x *= -0.98

    if a.position.x >= -2.0 and a.position.x <= -1.9 and a.position.y <= 2.3 and a.position.y >= 1.3:
        a.velocity.x *= -0.98

    if a.position.x >= 1.9 and a.position.x <= 2.0 and a.position.y <= 2.3 and a.position.y >= 1.3:
        a.velocity.x *= -0.98

    if a.position.x <= -1.0 and a.position.x >= -2.0 and a.position.y  - a.radius <= 1.4 - 5/24 - 5/24 * (a.position.x + 1.0) and a.position.y + a.radius >= 1.3 - 5/24 - 5/24 * (a.position.x + 1.0):
        wallAngle = Vec(5,24,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle
        #a.position.y = 0.1 - 5/24 * a.position.x + a.radius

    if a.position.x >= 1.0 and a.position.x <= 2.0 and a.position.y  - a.radius <= 1.4 - 5/24 + 5/24 * (a.position.x - 1.0) and a.position.y  + a.radius >= 1.3 - 5/24 + 5/24 * (a.position.x - 1.0):
        wallAngle = Vec(-5,24,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle
        #a.position.y = 0.1 + 5/24 * a.position.x + a.radius

    if a.position.x <= -1.4 and a.position.x >= -2.4 and a.position.y - a.radius <= 4 - 1/2 * (a.position.x + 1.4) and a.position.y  + a.radius >= 4:
        wallAngle = Vec(1,2,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle
    
    if a.position.x >= 1.4 and a.position.x <= 2.4 and a.position.y - a.radius <= 4 + 1/2 * (a.position.x - 1.4) and a.position.y + a.radius >= 4:
        wallAngle = Vec(-1,2,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle

    if a.position.x <= -1.4 and a.position.x >= -2.4 and a.position.y - a.radius < 4 and a.position.y + a.radius >= 4 + 1/2 * (a.position.x + 1.4):
        wallAngle = Vec(1,-2,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle

    if a.position.x >= 1.4 and a.position.x <= 2.4 and a.position.y - a.radius < 4 and a.position.y + a.radius >= 4 - 1/2 * (a.position.x - 1.4):
        wallAngle = Vec(-1,-2,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle

    

def stop(a):

    dist_hole = (a.position - HOLE).mag()
    vmag = a.velocity.mag()
    
    if dist_hole < (0.054 - 0.032 * vmag):
        a.visible=False

def move(a,n):
    for i in range(n):
        if run:
            a.acceleration=forces(a)/a.mass
            a.velocity+=a.acceleration*dt
            a.position+=a.velocity*dt
            edges(a)
            collision(a)
            stop(a)