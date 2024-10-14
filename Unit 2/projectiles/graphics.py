#render

import pygame as pg
import physics as phys


scale=10 #how many pixels are in a meter

def setup(w,h):

    global screen
    global clock
    pg.init()
    screen=pg.display.set_mode((w,h))
    pg.display.set_caption("Projectiles")
    clock=pg.time.Clock()

def background():
    screen.fill((200, 225, 250))
    pg.draw.rect(screen, (180, 255, 180), (0, 500, 800, 100))

def render(a):
    #background()
    pg.draw.circle(screen,(0,0,0),(scale*a.pos.x,500-1*scale*a.pos.y),5)
    pg.display.flip()

def frameRate(a):
    clock.tick(a)

def check_interactions():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            phys.run=False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                phys.go = True        

