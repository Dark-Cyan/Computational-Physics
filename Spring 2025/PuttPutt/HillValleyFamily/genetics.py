#fitness algorithm

import pop
import random
from vectors import*
from operator import attrgetter

standarddeviation = 0.05
threshhold = False

def offspring(a, n):
    #I want "n" offspring of object "a"
    for i in range(n):
        ball = pop.Ball(Vec(random.gauss(a.initVel.x, standarddeviation),random.gauss(a.initVel.y, standarddeviation),0), a.color)
        pop.population.append(ball)

def next_gen():
    global standarddeviation
    global threshhold
    if len(pop.winners) + len(pop.losers)==pop.populationSize:
        pop.population.clear()
        #pop.lander.sort(key = lambda f: f.range, reverse = True)
        pop.winners.sort(key = (attrgetter('speed')), reverse = False)
        pop.losers.sort(key = (attrgetter('distance')), reverse = False)
        pop.final = pop.winners + pop.losers
        print(pop.final[0].distance, pop.final[0].speed)
        offspring(pop.final[0],int(pop.populationSize*0.50 - 1))
        offspring(pop.final[1],int(pop.populationSize*0.20))
        offspring(pop.final[2],int(pop.populationSize*0.20))
        offspring(pop.final[3],int(pop.populationSize*0.10))
        ball = pop.Ball(pop.final[0].initVel, pop.final[0].color)
        pop.population.append(ball)
        pop.winners.clear()
        pop.losers.clear()
        pop.final.clear()