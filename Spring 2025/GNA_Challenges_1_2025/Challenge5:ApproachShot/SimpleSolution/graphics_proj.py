#render

import pygame as pg
import pop


view = True
run = False
s=1 #how many pixels are in a meter

def scale(a):
    return(a*s)

def setup(w,h):

    global screen
    global clock
    pg.init()
    screen=pg.display.set_mode((w,h))
    pg.display.set_caption("Projectile_GnA")
    clock=pg.time.Clock()

def background():
    screen.fill((200, 225, 250))
    pg.draw.rect(screen, (180, 255, 180), (0, 500, 800, 100))

def render():
    background()
    for i in pop.launcher:
        pg.draw.circle(screen,(0,0,0),(scale(i.pos.x),500-1*scale(i.pos.y)),2)
    clock.tick(60)
    pg.display.flip()

def check_interactions():
    global run,view
    for event in pg.event.get():
        if event.type == pg.QUIT:
            view = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                run = True
