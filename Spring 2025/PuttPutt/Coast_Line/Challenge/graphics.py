import pygame as pg
import pop
import physics as px
from vectors import Vec

 
# Global configuration
VIEW = True
S = 100  # how many pixels per meter

def scale(vec: Vec) -> tuple[int, int]:

    return (int(S * vec.x) + 300, 700 - int(S * vec.y))

def setup(width: int, height: int) -> None:
    #Initialize the pygame display and clock
    global screen, clock
    pg.init()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Coast Line")
    clock = pg.time.Clock()

def background() -> None:
    #Draws the background and the hole.
    screen.fill((60, 160, 80))
    pg.draw.circle(screen, (0, 0, 0), scale(px.HOLE), int(S * 0.054))
    pg.draw.rect(screen,(80,120,255),(0,0,6*S,1.75*S))

def render() -> None:
    background()
    for i in range(len(pop.population)):
        if isinstance(pop.population[i], pop.Family):
            for j in range(len(pop.population[i].familyMembers)):
                if pop.population[i].familyMembers[j].visible == True:
                    pg.draw.circle(screen, pop.population[i].familyMembers[j].color,scale(pop.population[i].familyMembers[j].pos), int(S * pop.population[i].familyMembers[j].r))
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