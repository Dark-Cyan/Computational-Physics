from vectors import*
import random
import math
import time
import organism
import os

run = False
startTime = time.time()

#Constants
timer = 0
dt = organism.dt

def move(a,n):
    for i in range(n):
        if run:
            a.setTarget()
            a.pos += (a.nextPos - a.pos).norm() * (a.speed - a.numBodySegments * 0.5) * dt
            a.bodySegments[0].pos = a.pos
            for j in range(1,len(a.bodySegments)):
                hi = 1
                a.bodySegments[j].pos = (a.bodySegments[j].pos - a.bodySegments[j-1].pos).norm() * a.bodySegments[j-1].r + a.bodySegments[j-1].pos
        a.hunger -= a.speed ** 2 * dt / 1000
        a.thirst -= a.speed ** 2 * dt / 1000
        a.timer += dt / 5
        a.interact()
    if a.hunger <= 0 or a.thirst <= 0:
        organism.organisms.remove(a)
        organism.speeds.remove(a.speed)
        organism.visions.remove(a.vision)
        organism.totalBodySegments.remove(a.numBodySegments)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Population:", len(organism.organisms))
        print("Average Speed:", sum(organism.speeds)/len(organism.speeds))
        print("Average Vision:", sum(organism.visions)/len(organism.visions))
        print("Average Body Segments", sum(organism.totalBodySegments)/len(organism.totalBodySegments))