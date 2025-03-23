import pygame as pg
import pop
import physics as px
from vectors import Vec
import random
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

    # Draws the background and the hole.
    screen.fill((60, 160, 80))
    # pg.draw.circle(screen, (0, 0, 0), scale(px.HOLE), int(S * 0.054))
    # for hill in px.HILLS:
    #     pg.draw.circle(screen, (66, 176, 88), scale(hill), int(S * px.HILL_R))
    # border_color = (120, 120, 120)

    #WALL INFORMATION
    # pg.draw.rect(screen, border_color, (
    #     int(S * px.RWALL_T.x) + 300,
    #     700 - int(S * px.RWALL_T.y),
    #     int(0.1 * S),
    #     int(px.RWALL_length * S)
    # ))
    # pg.draw.rect(screen, border_color, (
    #     int(S * px.LWALL_T.x) + 300,
    #     700 - int(S * px.LWALL_T.y),
    #     int(0.1 * S),
    #     int(px.LWALL_length * S)
    # ))
    # pg.draw.rect(screen, border_color, (
    #     int(S * px.BWALL_T.x) + 300,
    #     700 - int(S * px.BWALL_T.y),
    #     int(0.1 * S),
    #     int(px.BWALL_length * S)
    # ))

    pg.draw.rect(screen, (0, 0, 0), (0,0,10,800)) #Left Wall
    pg.draw.rect(screen, (0, 0, 0), (590,0,10,800)) #Right Wall
    pg.draw.rect(screen, (0, 0, 0), (0,0,600,10)) #Top Wall
    pg.draw.rect(screen, (0, 0, 0), (0,790,600,10)) #Bottom Wall

    pg.draw.rect(screen, (0, 0, 0), (550,155,10,645)) #Launcher Wall

    pg.draw.arc(screen, (0, 0, 0), (445, 10, 145, 145), 0, math.pi/2) #Top Right Curve
    pg.draw.arc(screen, (0, 0, 0), (10, 10, 145, 145), math.pi/2, math.pi) #Top Left Curve

    pg.draw.polygon(screen, (0, 0, 0), [(10, 740),(10,790),(280,790)]) #Bottom Left Triangle
    pg.draw.polygon(screen, (0, 0, 0), [(550, 740),(550,790),(280,790)]) #Bottom Right Triangle

    #FLIPPERS
    pg.draw.lines(screen, (0, 0, 0), False, [(60, 570), (60, 670), (180, 700)]) #Left Guide
    pg.draw.lines(screen, (0, 0, 0), False, [(500, 570), (500, 670), (380, 700)]) #Right Guide
    pg.draw.polygon(screen, (0, 0, 0), [(180, 700), (260, 720), (180, 740)]) #Left Flipper
    pg.draw.polygon(screen, (0, 0, 0), [(380, 700), (300, 720), (380, 740)]) #Right Flipper

    #BUMPERS
    pg.draw.circle(screen, (0, 0, 0), (280, 400), 50) #Center Circle
    pg.draw.polygon(screen, (0, 0, 0), [(90, 570), (90, 640), (180, 670)]) #Left Bumper
    pg.draw.polygon(screen, (0, 0, 0), [(470, 570), (470, 640), (380, 670)]) #Left Bumper


def render() -> None:
    background()
    if pop.ball.visible==True:
        pg.draw.circle(screen, (255, 255, 255), scale(pop.ball.pos), int(S * pop.ball.r))
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