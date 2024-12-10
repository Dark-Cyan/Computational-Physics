#graphics.py

import pygame as pg
import physics as p

run = True
w = 800
h = 600

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
    pg.draw.rect(screen, (240, 250, 255), (0, h - 140, w, h))

def render():
    #hello
    hi = 1

def frameRate(a):
    clock.tick(a)

def check_interactions():
    global run
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type==pg.KEYDOWN:
            hello = 1

setup()



while run:
    frameRate(60)
    check_interactions()
    background()
    render()
    #p.move(10)
    pg.display.flip()

pg.quit()