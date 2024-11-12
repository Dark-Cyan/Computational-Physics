#render
import pygame as pg
import physics as phys

scale=1E-9 #how many pixels are in a meter
focusx=0
focusy=0
focusNum=0

def setup(w,h):

    global screen
    global clock
    global focusx, focusy
    pg.init()
    screen=pg.display.set_mode((w,h))
    pg.display.set_caption("Projectiles")
    clock=pg.time.Clock()
    focusx=screen.get_width()/2
    focusy=screen.get_height()/2

def background():
    screen.fill((0, 0, 0))

#def fixFocus():
#    global focusNum
#    if focusNum < 0:
#        focusNum = len(list) - focusNum
#    focusNum %= len(list) + 1

#def shiftFocus(list):
#    global focusx, focusy, focusNum
#    fixFocus()
#    if focusNum == 0:
#        focusx=screen.get_width()/2
#        focusy=screen.get_height()/2
#    else:
#        focusx = list[focusNum].pos.x
#        focusy = list[focusNum].pos.y

def render(list):
    #shiftFocus(list)
    background()
    for i in range(len(list)):
        for j in range(list[i].recpos.qsize()):
            current = list[i].recpos.get()
            list[i].recpos.put(current)
            pg.draw.circle(screen,(255,255,255),(scale*current.x+focusx,focusy-scale*current.y),1)
        pg.draw.circle(screen,list[i].color,(scale*list[i].pos.x+focusx,focusy-scale*list[i].pos.y),list[i].r/10)
    pg.display.flip()

def frameRate(a):
    clock.tick(a)

def check_interactions():
    global scale, focusNum
    for event in pg.event.get():
        if event.type == pg.QUIT:
            phys.run=False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                phys.go = True
            elif event.key == pg.K_RIGHT:
                focusNum += 1
            elif event.key == pg.K_LEFT:
                focusNum -= 1
        if event.type == pg.MOUSEWHEEL:
            scale *= 1.5**event.y
