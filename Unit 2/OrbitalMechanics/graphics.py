#render
import pygame as pg
import physics as phys


scale=1E-9 #how many pixels are in a meter

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
        for j in range(list[i].recpos.qsize()):
            current = list[i].recpos.get()
            list[i].recpos.put(current)
            pg.draw.circle(screen,(255,255,255),(scale*current.x+screen.get_width()/2,screen.get_height()/2-scale*current.y),1)
        pg.draw.circle(screen,list[i].color,(scale*list[i].pos.x+screen.get_width()/2,screen.get_height()/2-scale*list[i].pos.y),list[i].r/10)
    pg.display.flip()

def frameRate(a):
    clock.tick(a)

def check_interactions():
    global scale
    for event in pg.event.get():
        if event.type == pg.QUIT:
            phys.run=False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                phys.go = True
        if event.type == pg.MOUSEWHEEL:
            scale *= 1.5**event.y
