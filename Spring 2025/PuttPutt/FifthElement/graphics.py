import pygame as pg
from vectors import Vec
import golfBall
import physics as px
import math

# Global configuration
VIEW = True
S = 100  # how many pixels per meter

def scale(vec: Vec) -> tuple[int, int]:
    # Convert simulation coordinates to screen coordinates
    return (int(S * vec.x) + 250, 800 - int(S * vec.y))

def scaleX(num: int) -> int:
    return int(S * num) + 250

def scaleY(num: int) -> int:
    return 800 - int(S * num)

def setup(width: int, height: int) -> None:
    global screen, clock, texture  # Make texture global
    pg.init()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Chaos")
    clock = pg.time.Clock()

 
def background() -> None:
    #Colors
    magenta = (139, 0, 139)

    screen.fill((0, 0, 0))

    #Background
    pg.draw.circle(screen, magenta, scale(Vec(0.25, 5.25, 0)), S * 2.65)
    pg.draw.rect(screen, magenta, (scaleX(-2.4), scaleY(5.25), 530, 515))
    pg.draw.polygon(screen, (0, 0, 0), [scale(Vec(-2.4, 0.6, 0)), scale(Vec(-2.4, 0.1, 0)), scale(Vec(0, 0.1, 0))])
    pg.draw.polygon(screen, (0, 0, 0), [scale(Vec(2.4, 0.6, 0)), scale(Vec(2.4, 0.1, 0)), scale(Vec(0, 0.1, 0))])

    pg.draw.circle(screen, (0, 0, 0), scale(Vec(0, 0.15, 0)), int(S * 0.054))

    pg.draw.rect(screen, (0, 0, 0), (scaleX(2.4), scaleY(6), 10, 600))

    #pg.draw.polygon(screen, (0, 0, 0), [(10, 740),(10,790),(280,790)]) #Bottom Left Triangle

    #Current Bumper:
    circleBumperPos = Vec(0, 4, 0)
    circleBumperRad = 0.5
    pg.draw.circle(screen, (0, 0, 0), scale(circleBumperPos), S * circleBumperRad)

    pg.draw.rect(screen, (0, 0, 0), (scaleX(-2.0), scaleY(2.3), 10, 100))
    pg.draw.rect(screen, (0, 0, 0), (scaleX(1.9), scaleY(2.3), 10, 100))
    


def render() -> None:
    background()
    if golfBall.ball.visible==True:
        pg.draw.circle(screen, golfBall.ball.color, scale(golfBall.ball.position), int(S * golfBall.ball.radius))
    clock.tick(60)
    pg.display.flip()

def check_interactions() -> None:
    global VIEW
    for event in pg.event.get():
        if event.type == pg.QUIT:
            VIEW = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                px.run = True