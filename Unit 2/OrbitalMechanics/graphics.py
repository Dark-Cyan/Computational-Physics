#render
import pygame as pg
import physics as phys


scale=1 #how many pixels are in a meter

def setup(w,h):

    global screen
    global clock
    pg.init()
    screen=pg.display.set_mode((w,h))
    pg.display.set_caption("Projectiles")
    clock=pg.time.Clock()

def background():
    screen.fill((0, 0, 0))

def render(list):
    background()
    for i in range(len(list)):
        pg.draw.circle(screen,list[i].color,(scale*list[i].pos.x+screen.get_width()/2,screen.get_height()/2-scale*list[i].pos.y),5)
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
