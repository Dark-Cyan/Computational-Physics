#fitness algorithm

import pop
import random
from operator import attrgetter

standarddeviation = 1
threshhold =False

def offspring(a, n):
    #I want "n" offspring of object "a"
    for i in range(n):
        ball = pop.Ball(23,random.gauss(a.speed,standarddeviation), 0, 0)
        pop.launcher.append(ball)

def next_gen():
    global standarddeviation
    global threshhold
    if len(pop.lander)==pop.repeats:
        #pop.lander.sort(key = lambda f: f.range, reverse = True)
        pop.lander.sort(key = (attrgetter('distance')), reverse = False)
        print(pop.lander[0].range, pop.lander[0].speed)
        offspring(pop.lander[0],499)
        offspring(pop.lander[1],300)
        offspring(pop.lander[2],100)
        offspring(pop.lander[3],100)
        ball = pop.Ball(23, pop.lander[0].speed, 250, 0)
        pop.launcher.append(ball)
        pop.lander.clear()