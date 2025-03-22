from vectors import*
import pop
import random

#Physics engine

##Switches - Booleans##
run = False

# Course Constants

#Hole

HOLE=Vec(-2.5,-0.5,0)

#Hill

Hill=Vec(3,6,0)
Hill_R=4

# Walls

OUT=Vec(0,0,1)

#right wall
TRWALL=Vec(-0.95,3,0)
TRWALL_R=0.05
BRWALL=Vec(-0.95,-5,0)
RWALL_B= Vec(-1,-5,0)
RWALL_T=Vec(-1,3,0)
RWALL_length=(TRWALL-BRWALL).mag()
RWALL_norm1= (RWALL_T-RWALL_B).cross(OUT).norm()
RWALL_norm2= (RWALL_B-RWALL_T).cross(OUT).norm()

#left wall

TLWALL=Vec(-2.95,4,0)
TLWALL_R=0.05
BLWALL=Vec(-2.95,1,0)
BLWALL_R=0.05
LWALL_B= Vec(-3,1,0)
LWALL_T=Vec(-3,4,0)
LWALL_length=(LWALL_B-LWALL_T).mag()
LWALL_norm= (LWALL_B-LWALL_T).cross(OUT).norm()


#spray=0.3
spray=0
#cor,cor_range=0.7,0.01
cor,cor_range=0.7,0

#time and step
t=0
dt=0.001

# Forces

FRIC=0.025

def friction(a):

    try: 
        return -1*a.vel.norm()*FRIC
    except ValueError:
        return Vec(0, 0, 0)

def hill_slope(a):

    hill_force = Vec(0, 0, 0)
    direction = (a.pos - Hill).norm()
    distance = (a.pos - Hill).mag()
    if distance < Hill_R:
        if distance < Hill_R / 2:
            hill_force = 0.25*direction * distance
        else:
            hill_force = 1*direction * (1 / distance)

    return hill_force

def forces(a):
    return friction(a)+hill_slope(a)

def stop(a):

    dist_hole = (a.pos - HOLE).mag()

    if (a.pos-HOLE).mag() < (0.054-0.032*a.vel.mag()):
        a.pos = HOLE
        a.visible=False
        a.run = False
        a.distance = 0
        pop.finished += 1
        a.score = a.speed
        return True

    elif a.vel.mag()<0.01 and a.acc.mag()<0.6:
        a.vel=Vec(0,0,0)
        a.run = False
        pop.finished += 1
        a.distance = dist_hole
        a.score = a.distance + a.speed
        past_wall(a)
        return True
    
    elif abs(a.pos.x) > 3 or a.pos.y < -1 or a.pos.y > 7:
        a.run = False
        pop.finished += 1
        a.distance = dist_hole
        a.score = dist_hole + a.speed + abs(a.vel) * 3
        a.vel=Vec(0,0,0)
        past_wall(a)
        return True

def past_wall(a):
    if a.pos.x >= -0.95:
        a.score += 1000

def edge(a,edge):
    cir_norm=(a.pos-edge).norm()
    a.pos+=cir_norm*0.1
    a.vel-=1.5*a.vel.dot(cir_norm)*cir_norm


def detect_Rwall(a):
    d=(a.pos-TRWALL).mag()+(a.pos-BRWALL).mag()
    if d < RWALL_length+0.1:
        if RWALL_B.y<a.pos.y<RWALL_T.y:
                if a.pos.x-a.r>-0.95:
                    if a.pos.x-a.r<-0.9:
                        collision(a,RWALL_norm1)
                elif a.pos.x+a.r<-0.95:
                    if a.pos.x+a.r>-1:
                        collision(a,RWALL_norm2)
        elif (a.pos-TRWALL).mag()-a.r<TRWALL_R:
            edge(a,TRWALL)
    else:
        pass

def detect_Lwall(a):

    d=(a.pos-TLWALL).mag()+(a.pos-BLWALL).mag()
    if d < LWALL_length+0.05:
        if a.pos.x<LWALL_B.x+0.1+a.r and LWALL_B.y<a.pos.y<LWALL_T.y:
            collision(a,LWALL_norm)
        elif (a.pos-BLWALL).mag()-a.r<BLWALL_R:
            edge(a,BLWALL)
        elif (a.pos-TLWALL).mag()-a.r<TLWALL_R:
            edge(a,TLWALL)
    else:
        pass

def collision(a,wall_norm):

    a.pos-=a.vel*dt
    cWALLnorm=wall_norm.rot2D(random.gauss(0,spray))
    speedloss=random.uniform(cor-cor_range,cor+cor_range)
    Pspeed=a.vel.dot(cWALLnorm)
    bounce=2*speedloss*Pspeed*cWALLnorm
    a.vel-=bounce


def detect_walls(a):
    detect_Rwall(a)
    detect_Lwall(a) 

def move(a,n):
    global run
    for i in range(n):
        if run and a.run:
            a.acc=forces(a)/a.m
            a.vel+=a.acc*dt
            a.pos+=a.vel*dt
            detect_walls(a)
            if (stop(a)):
                break