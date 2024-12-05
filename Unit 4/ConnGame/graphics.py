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
    pg.display.set_caption("Lunar Lander")
    clock = pg.time.Clock()
    background_image = pg.image.load("deep_space.jpg").convert()

def background():
    screen.blit(background_image, (0, 0))
    pg.draw.rect(screen, (240, 250, 255), (0, h - 140, w, h))

def render():
    x = w / 2 + p.lander.pos.x
    y = h / 2 - p.lander.pos.y
    points = [
        (x, y),
        (x - 5, y + 20),
        (x - 5, y + 40),
        (x - 10, y + 38),
        (x - 10, y + 45),
        (x - 5, y + 40),
        (x - 10, y + 60),
        (x + 10, y + 60),
        (x + 5, y + 40),
        (x + 10, y + 38),
        (x + 10, y + 45),
        (x + 5, y + 40),
        (x + 5, y + 20)
    ]
    pg.draw.polygon(screen, (100, 255, 255), points)

    if p.lander.thrust_up:
        pg.draw.polygon(screen, (255,0,0), ((x-8,y+60), (x,y+80),(x+8,y+60)))

def frameRate(a):
    clock.tick(a)

def check_interactions():
    global run
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_UP:
                p.lander.thrust_up=True
        if event.type==pg.KEYUP:
            if event.key==pg.K_UP:
                p.lander.thrust_up=False

setup()

while run:
    frameRate(60)
    check_interactions()
    background()
    render()
    p.move(10)
    pg.display.flip()

pg.quit()