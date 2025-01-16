#fitness algorithm

import pop
import random
from operator import attrgetter

standarddeviation = 10
threshhold =False

def offspring(a, n):
    #I want "n" offspring of object "a"
    for i in range(n):
        ball = pop.Ball(random.gauss(a.angle,standarddeviation), 42, 0, 0)
        pop.launcher.append(ball)

def next_gen():
    global standarddeviation
    global threshhold
    if len(pop.lander)==pop.repeats:
        #pop.lander.sort(key = lambda f: f.range, reverse = True)
        pop.lander.sort(key = attrgetter('range'), reverse = True)
        print(pop.lander[0].range, pop.lander[0].angle)
        offspring(pop.lander[0],499)
        offspring(pop.lander[1],300)
        offspring(pop.lander[2],100)
        offspring(pop.lander[3],100)
        ball = pop.Ball(pop.lander[0].angle, 42, 0, 0)
        pop.launcher.append(ball)
        pop.lander.clear()
        standarddeviation *= 0.5
        if (standarddeviation <= 0.01):
            threshhold = True