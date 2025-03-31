import pygame as pg
from vectors import Vec
import math

# Global configuration
VIEW = True
S = 100  # how many pixels per meter

def scale(vec: Vec) -> tuple[int, int]:
    # Convert simulation coordinates to screen coordinates
    return (int(S * vec.x) + 300, 700 - int(S * vec.y))

def setup(width: int, height: int) -> None:
    global screen, clock, texture  # Make texture global
    pg.init()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Chaos")
    clock = pg.time.Clock()

 
def background() -> None:
    screen.fill((60, 160, 80))


def render() -> None:
    background()
    # if pop.ball.visible==True:
    #     pg.draw.circle(screen, (255, 255, 255), scale(pop.ball.newPos), int(S * pop.ball.r))
    # clock.tick(60)
    pg.display.flip()

def check_interactions() -> None:
    global VIEW
    for event in pg.event.get():
        if event.type == pg.QUIT:
            VIEW = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                #px.run = True
                hello = 1