import pygame 
import sys

sWidth = 1000
sHeight = 500

screen = pygame.display.set_mode([sWidth, sHeight])
screen.fill((150,200,255))

radius = 25
ball = pygame.draw.circle(screen, (40,132, 10), (sWidth/2, radius/2), radius)

run = True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
    pygame.display.flip()
pygame.quit()
sys.exit()