#graphics.py

import pygame as pg
import physics as p
import time

run = True
w = 800
h = 600
dropTimer = time.time()

def setup():
    global screen
    global clock
    global background_image
    pg.init()
    screen = pg.display.set_mode((w, h))
    pg.display.set_caption("Suika Game")
    clock = pg.time.Clock()
    #background_image = pg.image.load("deep_space.jpg").convert()

def background():
    #screen.blit(background_image, (0, 0))
    screen.fill((0,0,0))
    pg.draw.rect(screen, (240, 250, 255), (0, h - 140, w, h))

def render(list):
    for i in list:
        pg.draw.circle(screen, (255,0,0), (w/2+i.pos.x,h/2-i.pos.y), 10)

def frameRate(a):
    clock.tick(a)

def check_interactions():
    global run
    global dropTimer
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type==pg.KEYDOWN:
            hello = 1
        if event.type ==pg.MOUSEBUTTONDOWN:
            if (time.time() - dropTimer < 0.5):
                continue
            x, y = event.pos
            fruit = p.stuff(2, 10, p.Vec(x - w/2,h/5,0), p.Vec(0,-9.8,0), False)
            dropTimer = time.time()

setup()

while run:
    frameRate(60)
    check_interactions()
    background()

    p.move(p.fruits,1)
    render(p.fruits)

    pg.display.flip()

pg.quit()

#normalize the vector and dot it with original 