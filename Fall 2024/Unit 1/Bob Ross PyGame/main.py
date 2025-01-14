import pygame as pg
import sys

pg.init()

width = 800
height = 600

screen = pg.display.set_mode([width,height]) 
screen.fill((150,200,255))

pg.draw.rect(screen,(20,200,20), (0,0.8*height,width,0.2*height))
radius = 50
pg.draw.circle(screen,(253, 184, 19), (3/2*radius,3/2*radius), radius)
pg.draw.ellipse(screen, (255,255,255), (500,90,200,150))

pg.display.set_caption("Bob Ross was Here")

#Make a person
pg.draw.circle(screen, (224, 194, 152), (width/2, height/2), 70)
pg.draw.arc(screen, (0, 0, 0), (width/2,height/2,15, 15), 0, 2, 2)

run = True
while run:
    for i in pg.event.get():
        if i.type==pg.QUIT:
            run=False
    pg.display.flip()
pg.quit()
sys.exit()