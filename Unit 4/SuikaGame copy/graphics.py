#graphics.py

#Import Files
import pygame as pg
import physics as p
import game_logic as gl
import time
import random
import math

#Game Constants
run = True
w = 570
h = 770

#Timers
dropTimer = time.time()


#Fruit Constants
COLORS = [
    (245,0,0),
    (250,100,100),
    (150,20,250),
    (250,210,10),
    (250,150,0),
    (245,0,0),
    (250,250,100),
    (255,180,180),
    (255,255,0),
    (100,235,10),
    (0,185,0)
]
RADII = [17,25,32,38,50,63,75,87,100,115,135]
Density = 0.001
POINTS = [1,3,6,10,15,21,28,36,45,55,66]

#Sets up the screen for the game
def setup():
    global screen
    global clock
    global background_image
    pg.init()
    screen = pg.display.set_mode((w, h))
    pg.display.set_caption("Suika Game")
    clock = pg.time.Clock()
    background_image = pg.image.load('back.png')

#draws the background and the container for the fruit
def background():
    screen.fill((0,0,0))
    screen.blit(background_image, (0, 0))
    width = w/2
    height = h/2
    border = [
        (width-200,height-320),
        (width-210,height-320),
        (width-210,height+330),
        (width+210,height+330),
        (width+210,height-320),
        (width+200,height-320),
        (width+200, height+320),
        (width-200,height+320)
    ]
    pg.draw.polygon(screen, (255,255,255), border)
    pg.draw.line(screen, (105,105,105), (width-200,height-280), (width+200,height-280), 3)

#draws all the fruit objects
def render(list):
    for i in list:
        pg.draw.circle(screen, i.col, (w/2+i.pos.x,h/2-i.pos.y), i.r)      

#sets framerate of the game
def frameRate(a):
    clock.tick(a)

#checks for keyboard/mouse inputs
def check_interactions():
    global run
    global dropTimer
    global currentFruit
    for event in pg.event.get(): #if quit then quit
        if event.type == pg.QUIT:
            run = False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_r: #if r is pressed reset the game
                game.reset()
                p.points.clear()
                p.fruits.clear()
                currentFruit = p.stuff(Density*math.pi*(RADII[0]**2), RADII[0], p.Vec(mouseX,330,0), p.Vec(0,0,0), p.Vec(0,-9.8,0), True, COLORS[0], 0)
        if event.type ==pg.MOUSEBUTTONDOWN: #if mouse is pressed summon fruit
            if (time.time() - dropTimer < 1): #if not enough time has passed since most recent drop contine
                continue
            x, y = event.pos
            currentFruit.anchor = False #unanchors currentFruit
            
            #creates a new random current fruit and sets its position temporarily far off screen
            randomFruit = random.randint(0,3)
            currentFruit = p.stuff(Density*math.pi*(RADII[randomFruit]**2), RADII[randomFruit], p.Vec(100000,330,0), p.Vec(0,0,0), p.Vec(0,-9.8,0), True, COLORS[randomFruit], randomFruit)
            #sets drop timer to current time
            dropTimer = time.time()

#draws text to the screen at pos x and y
def draw_text(text, text_col, x, y):
    font = pg.font.SysFont(None, 50)
    image = font.render(text, True, text_col)
    screen.blit(image, (x,y))

#starts the game up
game  = gl.Game()
setup()
mouseX,mouseY = pg.mouse.get_pos()
currentFruit = p.stuff(Density*math.pi*(RADII[0]**2), RADII[0], p.Vec(mouseX,330,0), p.Vec(0,0,0), p.Vec(0,-9.8,0), True, COLORS[0], 0)


while run: #main loop of the game
    frameRate(60) #sets frame rate to 60
    check_interactions() #check interactions

    if game.state == 'play': #loop to run if state is play
        background()
        draw_text(("Score: " + str(sum(p.points))), (255,255,255), 0,0)

        #if enough time has passed since last drop, let current ball track onto mouse position
        if (time.time() - dropTimer > 0.9):
            game.updatePoints(p.points)
            currentX = pg.mouse.get_pos()[0] - w/2
            if currentX - currentFruit.r <= -200:
                currentX = -200 + currentFruit.r
            elif currentX + currentFruit.r >= 200:
                currentX = 200 - currentFruit.r
            currentFruit.pos.x = (currentX)

        #moves the fruits
        p.move(p.fruits,10)

        #if there is a ball outside of the container notify the game object
        check = 0
        for i in p.fruits:
            if i.anchor == True:
                hello = 1
            elif i.pos.y >= 280:
                game.overFlow(True)
                break
            check +=1
        if check == len(p.fruits):
            game.overFlow(False)

        #renders the fruit
        render(p.fruits)

        #if win is announced, update game state
        if p.win == True:
            game.win()

        #flip to screen
        pg.display.flip()
    elif game.state == 'lose': #loop to run if state is lose
        draw_text("GAME OVER", (0,157,196), 170,310)
        draw_text("\'r' to try again", (0,157,196), 160, 360)
        pg.display.flip()
    elif game.state == 'win': #loop to run if state is win
        draw_text("YOU WIN", (0,157,196), 180,310)
        draw_text("\'r' to try again", (0,157,196), 160, 360)
        pg.display.flip()

#quits pygam
pg.quit()
