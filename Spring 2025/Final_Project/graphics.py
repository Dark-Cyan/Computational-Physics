import pygame as pg
from vectors import Vec
import math

from organism import*

view = True
scaleCoefficient = 100  # how many pixels per meter

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
    pg.display.set_caption("Chaos")
    clock = pg.time.Clock()

 
def background() -> None:
    #Colors
    grassColor = (38,139,7)

    screen.fill(grassColor)

    organismPos = Vec(0,0,0)
    organismSize = 0.5
    pg.draw.circle(screen, (0, 0, 0), scale(organismPos), organismSize * scaleCoefficient)

def render() -> None:
    background()
    # for i in Organism.organisms:
    #     if i.visible==True:
    #         pg.draw.circle(screen, i.color, scale(i.position), int(S * i.radius))
    clock.tick(60)
    pg.display.flip()

def check_interactions() -> None:
    global view
    for event in pg.event.get():
        if event.type == pg.QUIT:
            view = False
        # elif event.type == pg.KEYDOWN:
        #     if event.key == pg.K_SPACE:
        #         px.run = True
        #         px.timer = 0