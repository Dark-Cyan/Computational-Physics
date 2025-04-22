import pygame as pg
from vectors import Vec
import math
from organism import organisms

view = True
scaleCoefficient = 100  # how many pixels per meter
#cameraState = "interactive"
cameraState = "following"

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
    pg.display.set_caption("Chaos")
    clock = pg.time.Clock()

 
def background() -> None:
    #Colors
    grassColor = (38,139,7)

    screen.fill(grassColor)

def render() -> None:
    background()
    for i in organisms:
        pg.draw.circle(screen, i.color, scale(i.position), int(scaleCoefficient * i.size))
    #if cameraState == "following":
        #dimensions = 
        #pg.draw.rect(screen, (255,255,255), (, scaleY(5.25), screen.get_width() * 0.1 * scaleCoefficient), screen.get_height() * 0.3 * scaleCoefficient)
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