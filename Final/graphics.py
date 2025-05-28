import pygame as pg
from vectors import Vec
import physics as px
import math
from organism import*
from water import*
from food import*

view = True
scaleCoefficient = 100  # how many pixels per meter

trueCenter = Vec(0,0,0)

def scale(vec: Vec) -> tuple[int, int]:
    # Convert simulation coordinates to screen coordinates
    return (int(scaleCoefficient * vec.x) + screen.get_width()/2, screen.get_height()/2 - int(scaleCoefficient * vec.y))

def scaleX(num: int) -> int:
    return int(scaleCoefficient * num) + screen.get_width()/2

def scaleY(num: int) -> int:
    return screen.get_height()/2 - int(scaleCoefficient * num)

def setup(width: int, height: int) -> None:
    global screen, clock, texture  # Make texture global
    pg.init()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Natural Selection")
    clock = pg.time.Clock()

 
def background() -> None:
    #Colors
    grassColor = (38,139,7)
    screen.fill(grassColor)
    for i in ponds:
        pg.draw.circle(screen, i.color, scale(i.pos), i.r * scaleCoefficient)
    # for i in organisms:
    #     pg.draw.circle(screen, (255,255,255), scale(i.pos), i.vision * scaleCoefficient)
    # for i in organisms:
    #     pg.draw.circle(screen, (0,0,0), scale(i.nextPos), i.size * scaleCoefficient)
    for i in foods:
        pg.draw.circle(screen, i.color, scale(i.pos), i.r * scaleCoefficient)

def render() -> None:
    background()
    for i in organisms:
        for j in i.bodySegments:
            pg.draw.circle(screen, i.color, scale(j.pos), j.r * scaleCoefficient)
    clock.tick(60)
    pg.display.flip()

def check_interactions() -> None:
    global view
    for event in pg.event.get():
        if event.type == pg.QUIT:
            view = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                px.run = True
                px.timer = 0