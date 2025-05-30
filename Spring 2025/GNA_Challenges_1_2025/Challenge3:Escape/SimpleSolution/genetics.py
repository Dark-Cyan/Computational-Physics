#fitness algorithm

import pop
import random
from operator import attrgetter

standarddeviation = 10
threshhold =False

def offspring(a, n):
    #I want "n" offspring of object "a"
    for i in range(n):
        ball = pop.Ball(90, random.gauss(a.speed,standarddeviation), 8848.86)
        pop.launcher.append(ball)

def next_gen():
    global standarddeviation
    global threshhold
    if len(pop.lander)==pop.repeats:
        #pop.lander.sort(key = lambda f: f.range, reverse = True)
        pop.lander.sort(key = (attrgetter('distance')), reverse = False)
        print(pop.lander[0].distance, pop.lander[0].speed)
        offspring(pop.lander[0],100)
        offspring(pop.lander[1],53)
        offspring(pop.lander[2],23)
        offspring(pop.lander[3],23)
        ball = pop.Ball(90, pop.lander[0].speed, 8848.86)
        pop.launcher.append(ball)
        pop.lander.clear()
        standarddeviation*=0.8