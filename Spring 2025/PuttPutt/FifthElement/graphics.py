import pygame as pg
from vectors import Vec
import golfBall
import physics as px
import math
import time

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
    pg.draw.circle(screen, (255, 255, 255), scale(circleBumperPos), S * (circleBumperRad - 0.05))

    pg.draw.rect(screen, (0, 0, 0), (scaleX(-2.0), scaleY(2.3), 10, 100))
    pg.draw.rect(screen, (0, 0, 0), (scaleX(1.9), scaleY(2.3), 10, 100))

    #Guides
    pg.draw.polygon(screen, (0, 0, 0), [scale(Vec(-2.0, 1.3, 0)), scale(Vec(-0.9, 1.3 - 5/24, 0)), scale(Vec(-0.9, 1.4 - 5/24, 0)), scale(Vec(-2.0, 1.4, 0))])
    pg.draw.polygon(screen, (0, 0, 0), [scale(Vec(2.0, 1.3, 0)), scale(Vec(0.9, 1.3 - 5/24, 0)), scale(Vec(0.9, 1.4 - 5/24, 0)), scale(Vec(2.0, 1.4, 0))])

    #Top Triangle Sides
    pg.draw.polygon(screen, (0, 0, 0), [scale(Vec(-2.4, 4.5, 0)), scale(Vec(-1.4, 4, 0)), scale(Vec(-1.5, 4, 0)), scale(Vec(-2.4, 4.4, 0))])
    pg.draw.polygon(screen, (0, 0, 0), [scale(Vec(2.4, 4.5, 0)), scale(Vec(1.4, 4, 0)), scale(Vec(1.5, 4, 0)), scale(Vec(2.4, 4.4, 0))])

    #Bottom Triangle Sides
    pg.draw.polygon(screen, (0, 0, 0), [scale(Vec(-2.4, 3.5, 0)), scale(Vec(-1.4, 4, 0)), scale(Vec(-1.5, 4, 0)), scale(Vec(-2.4, 3.6, 0))])
    pg.draw.polygon(screen, (0, 0, 0), [scale(Vec(2.4, 3.5, 0)), scale(Vec(1.4, 4, 0)), scale(Vec(1.5, 4, 0)), scale(Vec(2.4, 3.6, 0))])

    lflipperCenter = Vec(-0.95, 1.175, 0)#Vec(-0.9, 1.125, 0)
    lflipperAngle = math.cos(px.timer) * math.pi/4
    ltopCornerFlip = Vec(-0.95, 1.175, 0)
    lactTLF = Vec((ltopCornerFlip - lflipperCenter).x * math.cos(lflipperAngle) - (ltopCornerFlip - lflipperCenter).y * math.sin(lflipperAngle), (ltopCornerFlip - lflipperCenter).x * math.sin(lflipperAngle) + (ltopCornerFlip - lflipperCenter).y * math.cos(lflipperAngle), 0) + lflipperCenter
    lbottomCornerFlip = Vec(-0.95, 1.075, 0)
    lactBLF = Vec((lbottomCornerFlip - lflipperCenter).x * math.cos(lflipperAngle) - (lbottomCornerFlip - lflipperCenter).y * math.sin(lflipperAngle), (lbottomCornerFlip - lflipperCenter).x * math.sin(lflipperAngle) + (lbottomCornerFlip - lflipperCenter).y * math.cos(lflipperAngle), 0) + lflipperCenter
    lbottomEdgeFlip = Vec(-0.2, 1.075, 0)
    lactBRF = Vec((lbottomEdgeFlip - lflipperCenter).x * math.cos(lflipperAngle) - (lbottomEdgeFlip - lflipperCenter).y * math.sin(lflipperAngle), (lbottomEdgeFlip - lflipperCenter).x * math.sin(lflipperAngle) + (lbottomEdgeFlip - lflipperCenter).y * math.cos(lflipperAngle), 0) + lflipperCenter
    ltopEdgeFlip = Vec(-0.2, 1.175, 0)
    lactTRF = Vec((ltopEdgeFlip - lflipperCenter).x * math.cos(lflipperAngle) - (ltopEdgeFlip - lflipperCenter).y * math.sin(lflipperAngle), (ltopEdgeFlip - lflipperCenter).x * math.sin(lflipperAngle) + (ltopCornerFlip - ltopEdgeFlip).y * math.cos(lflipperAngle), 0) + lflipperCenter
    pg.draw.polygon(screen, (255, 174, 66), [scale(lactTLF), scale(lactBLF), scale(lactBRF), scale(lactTRF)])

    rflipperCenter = Vec(0.95, 1.175, 0) #Vec(0.9, 1.125, 0)
    rflipperAngle = math.cos(px.timer) * math.pi/4
    rtopCornerFlip = Vec(0.95, 1.175, 0)
    ractTLF = Vec((rtopCornerFlip - rflipperCenter).x * math.cos(rflipperAngle) - (rtopCornerFlip - rflipperCenter).y * math.sin(rflipperAngle), (rtopCornerFlip - rflipperCenter).x * math.sin(rflipperAngle) + (rtopCornerFlip - rflipperCenter).y * math.cos(rflipperAngle), 0) + rflipperCenter
    rbottomCornerFlip = Vec(0.95, 1.075, 0)
    ractBLF = Vec((rbottomCornerFlip - rflipperCenter).x * math.cos(rflipperAngle) - (rbottomCornerFlip - rflipperCenter).y * math.sin(rflipperAngle), (rbottomCornerFlip - rflipperCenter).x * math.sin(rflipperAngle) + (rbottomCornerFlip - rflipperCenter).y * math.cos(rflipperAngle), 0) + rflipperCenter
    rbottomEdgeFlip = Vec(0.2, 1.075, 0)
    ractBRF = Vec((rbottomEdgeFlip - rflipperCenter).x * math.cos(rflipperAngle) - (rbottomEdgeFlip - rflipperCenter).y * math.sin(rflipperAngle), (rbottomEdgeFlip - rflipperCenter).x * math.sin(rflipperAngle) + (rbottomEdgeFlip - rflipperCenter).y * math.cos(rflipperAngle), 0) + rflipperCenter
    rtopEdgeFlip = Vec(0.2, 1.175, 0)
    ractTRF = Vec((rtopEdgeFlip - rflipperCenter).x * math.cos(rflipperAngle) - (rtopEdgeFlip - rflipperCenter).y * math.sin(rflipperAngle), (rtopEdgeFlip - rflipperCenter).x * math.sin(rflipperAngle) + (rtopCornerFlip - rtopEdgeFlip).y * math.cos(rflipperAngle), 0) + rflipperCenter
    pg.draw.polygon(screen, (255, 174, 66), [scale(ractTLF), scale(ractBLF), scale(ractBRF), scale(ractTRF)])

    miniBump1 = Vec(-0.35, 5.65, 0)
    miniBump2 = Vec(0, 6.35, 0)
    miniBump3 = Vec(0.35, 6, 0)
    miniBumpRad = 0.15
    pg.draw.circle(screen, (0, 0, 0), scale(miniBump1), miniBumpRad * S)
    pg.draw.circle(screen, (0, 0, 0), scale(miniBump2), miniBumpRad * S)
    pg.draw.circle(screen, (0, 0, 0), scale(miniBump3), miniBumpRad * S)
    pg.draw.circle(screen, (255, 255, 0), scale(miniBump1), (miniBumpRad - 0.05) * S)
    pg.draw.circle(screen, (0, 0, 255), scale(miniBump2), (miniBumpRad - 0.05) * S)
    pg.draw.circle(screen, (255, 0, 0), scale(miniBump3), (miniBumpRad - 0.05) * S)
    

def render() -> None:
    background()
    for i in golfBall.population:
        if i.visible==True:
            pg.draw.circle(screen, i.color, scale(i.position), int(S * i.radius))
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
                px.timer = 0