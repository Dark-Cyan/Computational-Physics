#fitness algorithm

import pop
import random
from operator import attrgetter

standarddeviation = 1
threshhold =False

def offspring(a, n):
    #I want "n" offspring of object "a"
    for i in range(n):
        ball = pop.Ball(random.gauss(a.angle, standarddeviation), 16)#random.gauss(a.backspin,standarddeviation))
        pop.launcher.append(ball)

def next_gen():
    global standarddeviation
    global threshhold
    if len(pop.lander)==pop.repeats:
        #pop.lander.sort(key = lambda f: f.range, reverse = True)
        pop.lander.sort(key = (attrgetter('range')), reverse = True)
        print(pop.lander[0].angle, pop.lander[0].speed, pop.lander[0].backspin, pop.lander[0].range)
        offspring(pop.lander[0],100)
        offspring(pop.lander[1],53)
        offspring(pop.lander[2],23)
        offspring(pop.lander[3],23)
        ball = pop.Ball(pop.lander[0].angle, 16)#pop.lander[0].backspin)
        pop.launcher.append(ball)
        pop.lander.clear()
        standarddeviation*=0.8