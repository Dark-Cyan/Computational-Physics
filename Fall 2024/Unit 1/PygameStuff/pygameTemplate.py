#Pygame Template

#this is terrible coding organization and usage:
import pygame as pg
import sys
import os

t=0
dt=0.1
pos=0
vel=0
force=800
mass=1000
acc=force/mass #newton's 2nd law

pg.init()

w=800
h=600

screen=pg.display.set_mode((w,h))
pg.display.set_caption("Name")
clock=pg.time.Clock()
run=True

while run: #main loop "game loop"
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                run=False
    clock.tick(60)
    screen.fill((200,225, 250))
    pg.draw.rect(screen, (180,255,180), (0,h-100,w,100))
    pg.draw.rect(screen,(0,0,0),(10+pos,h-110,30,10))
    pg.display.flip()

    #physics stuff

    pos+=vel*dt
    vel+=acc*dt
    t+=dt
    acc=force/mass


pg.quit()
sys.exit()