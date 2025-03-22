#fitness algorithm

import pop
import random
from vectors import*
from operator import attrgetter

standardDeviation = 5
threshhold = False

newPopulation = []

def offspring(a, n):
    #I want "n" offspring of object "a"
    for i in range(n):
        color = (min(random.gauss(a.color[0], standardDeviation), 255), min(random.gauss(a.color[1], standardDeviation), 255), min(random.gauss(a.color[2], standardDeviation), 255))
        ball = pop.Ball(Vec(a.ivel.x,random.gauss(a.ivel.y, standardDeviation),0), color)
        family = pop.Family(pop.children, ball, 0.05)
        newPopulation.append(family)

        

def next_gen():
    global standardDeviation
    global threshhold
    if pop.finished == pop.families + pop.families * pop.children:

        for i in pop.population:
            i.determineScore()
        pop.population.sort(key = (attrgetter('score')), reverse = False)

        offspring(pop.population[0].parent, int(pop.families*0.50 - 1))
        offspring(pop.population[1].parent, int(pop.families*0.3))
        offspring(pop.population[2].parent, int(pop.families*0.2))
        ball = pop.Ball(pop.population[0].parent.ivel, pop.population[0].parent.color)
        family = pop.Family(pop.children, ball, 0.05)
        newPopulation.append(family)
        print("_____________________________________________________________________________" + '\n')
        print("Best Group:", pop.population[0].parent.color, '\t', "Score:", pop.population[0].parent.score, '\t', "Distance:", (pop.population[0].distance/201))
        print("Best Individual:", pop.population[0].parent.color, '\t', "Distance:", pop.population[0].parent.distance, '\t', "Vx:", pop.population[0].parent.ivel.x, '\t', "Vy:", pop.population[0].parent.ivel.y)

        pop.population.clear()
        pop.population += newPopulation
        pop.finished = 0

        standardDeviation *= 0.75
        newPopulation.clear()