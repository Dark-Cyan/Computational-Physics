from vectors import*
from pop import ball
import random

#Physics engine

##Switches - Booleans##
run = False

# Course Constants

#HOLE

HOLE=Vec(0,-0.8,0)

#HILLS

HILLS=[] 
HILL_R=0.4

def odd_even_value(n):
    return 0 if n % 2 == 0 else 0.5

for i in range(-3,4,1):
    for j in range(1,6,1):
        HILL=Vec(i+odd_even_value(j),j+0.5,0)
        HILLS.append(HILL)

# Walls

OUT=Vec(0,0,1)

WALL_B= Vec(-3,-5,0)
WALL_T=Vec(-3,1,0)
WALL_length=(WALL_B-WALL_T).mag()

#right wall
TRWALL=Vec(2.5,7,0)
TRWALL_R=0.05
BRWALL=Vec(2.5,-1,0)
RWALL_B= Vec(2.45,-1,0)
RWALL_T=Vec(2.45,7,0)
RWALL_length=(TRWALL-BRWALL).mag()
RWALL_norm1= (RWALL_T-RWALL_B).cross(OUT).norm()
RWALL_norm2= (RWALL_B-RWALL_T).cross(OUT).norm()
 
#left wall

TLWALL=Vec(-2.95,7,0)
TLWALL_R=0.05
BLWALL=Vec(-2.95,-1,0)
BLWALL_R=0.05
LWALL_B= Vec(-3,-1,0)
LWALL_T=Vec(-3,7,0)
LWALL_length=(LWALL_B-LWALL_T).mag()
LWALL_norm= (LWALL_B-LWALL_T).cross(OUT).norm()

#bottom wall

TBWALL=Vec(-1.5,7,0)
TBWALL_R=0.5
BBWALL=Vec(-1.5,-1,0)
BBWALL_R=0.05
BWALL_B= Vec(-2,-1,0)
BWALL_T=Vec(-2,7,0)
BWALL_length=(BWALL_B-BWALL_T).mag()
BWALL_norm= (BWALL_B-BWALL_T).cross(OUT).norm()


#spray=0.3
spray=0
#cor,cor_range=0.7,0.01
cor,cor_range=0.7,0

t=0
dt=0.0006

# Forces

FRIC=0.025

def friction(a):
    #We haven't seen this yet. It's very nice, basically if what's in the
    #'try block' runs without error, then that's it, and the compiler moves on
    #otherwise it checks for the exceptions :)
    try: 
        return -1*a.vel.norm()*FRIC
    except ValueError:
        
        return Vec(0, 0, 0)

def hill_slope(a):

    hill_force = Vec(0, 0, 0)
    for hill in HILLS:
        direction = (a.pos - hill).norm()
        distance = (a.pos - hill).mag()
        if distance < HILL_R:
            if distance < HILL_R / 2:
                hill_force = 2.5*direction * distance
            else:
                hill_force = 0.1*direction * (1 / distance)

    return hill_force
        
def pinball_slope(a):
    return Vec(0,-0.05,0)

def forces(a):
    
    return friction(a)+hill_slope(a)+pinball_slope(a)

#WALL INFORMATION

def detect_wall(a):

    #d = (a.pos - WALL_T).mag() + (a.pos - WALL_B).mag()
    #if d < WALL_length + 0.05:

    #GAME BOUNDS
    if a.pos.x >= 2.95 or a.pos.x <= -2.95:
        print("HELP ME")
        a.bounce -= 10
        a.pos -= a.vel * dt
        a.vel.x *= -0.95
    if a.pos.y >= 6.95:
        print("YAY ME")
        a.bounce -= 10
        a.pos -= a.vel * dt
        a.vel.y *= -0.95
    
    #LAUNCH WALL
    if (a.pos.y <= 5.3 and a.pos.y >= -1 and a.pos.x - a.r <= 2.6 and a.pos.x + a.r >= 2.55):
        print("THE HUZZ")
        a.bounce -= 10
        a.pos -= a.vel * dt
        a.vel.x *= -0.95

    #if (a.pos.x >= -2.9 and a.pos.x <= -0.2 and a.pos.y)


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

def stop(a):

    dist_hole = (a.pos - HOLE).mag()
    vmag = a.vel.mag()
    
    if dist_hole < (0.054 - 0.032 * vmag):

        a.visible=False
        run = False
 
    elif vmag < 0.01 and a.acc.mag()<0.6:
        a.vel=Vec(0,0,0)
        run = False


def move(a,n):
    global run
    for i in range(n):
        if run:
            a.acc=forces(a)/a.m
            a.vel+=a.acc*dt
            a.pos+=a.vel*dt
            detect_wall(a)
            stop(a)