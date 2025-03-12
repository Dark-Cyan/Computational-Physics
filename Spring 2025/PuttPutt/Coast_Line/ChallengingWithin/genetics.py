#fitness algorithm

import pop
import random
from vectors import*
from operator import attrgetter

standardDeviation = 10
threshhold = False

def offspring(a, n):
    #I want "n" offspring of object "a"
    for i in range(n):
        ball = pop.Ball(Vec(random.gauss(a.initVel.x, standarddeviation),random.gauss(a.initVel.y, standarddeviation),0), a.color)
        

def next_gen():
    global standarddeviation
    global threshhold
    if pop.finished == pop.families + pop.families * pop.children:
        offspring(pop.population[0].parent, int(pop.families*0.50 - 1))
        offspring(pop.final[1],int(pop.populationSize*0.20))
        offspring(pop.final[2],int(pop.populationSize*0.20))
        ball = pop.Ball(pop.final[0].initVel, pop.final[0].color)
        pop.population.append(ball)
        standardDeviation *= 0.75