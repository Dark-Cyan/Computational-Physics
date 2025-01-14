# physics.py

from vectors import*
from stuff import Lander
import game_logic as gl

#constants intial stuff

g = Vec(0,-1.62,0)
t=0
dt=0.01

h = 200

cs=3

lander=Lander()
game=gl.Game()

def weight():
    return lander.m*g

def thrust():
    thrust=Vec(0,0,0)
    if lander.thrust_up:
        thrust+=Vec(0,2000,0)
    if lander.thrust_left:
        thrust+=Vec(-600,0,0)
    if lander.thrust_right:
        thrust+=Vec(600,0,0)
    return thrust

def forces():
    lander.force=weight()+thrust()

def move(reps):
    for i in range(reps):
        if game.state == 'play':
            forces()
            lander.acc=lander.force/lander.m
            lander.vel+=lander.acc*dt
            lander.pos+=lander.vel*dt
            collision()

def collision():
    if lander.pos.y <-100:
        game.state='stop'
        if lander.vel.mag()>cs:
            game.crash()
            game.lose()
        elif lander.vel.mag()<cs:
            game.land()
            game.win()