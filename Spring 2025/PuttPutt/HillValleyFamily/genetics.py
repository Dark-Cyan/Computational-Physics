#fitness algorithm

import pop
from pop import population
import random
from vectors import*
from operator import attrgetter

standarddeviation = 1
threshhold = False

def offspring(a, n, list, fn):
    #I want "n" offspring of object "a"
    for i in range(n):
        ball = pop.Ball(random.gauss(a.angle, standarddeviation),random.gauss(a.speed, standarddeviation), a.color, fn)
        list.append(ball)

def lowestHighest(list):
    minAngle = 180
    maxAngle = 180

def next_gen():
    global standarddeviation
    global threshhold
    if pop.finished==pop.populationSize:
        pop.finished = 0
        newPopulation = []
        # pop.population.clear()
        # pop.lander.sort(key = lambda f: f.range, reverse = True)
        
        # pop.winners.sort(key = (attrgetter('speed')), reverse = False)
        # pop.losers.sort(key = (attrgetter('distance')), reverse = False)
        fn = 0
        for i in population:
            i.familyMembers.sort(key = (attrgetter('distance')), reverse = False)

            #family = pop.Family(pop.populationSize/pop.families,, 1, i)

            family = []
            offspring(i.familyMembers[0],int(pop.populationSize/pop.families*0.50 - 1), family, fn)
            offspring(i.familyMembers[1],int(pop.populationSize/pop.families*0.20), family, fn)
            offspring(i.familyMembers[2],int(pop.populationSize/pop.families*0.20), family, fn)
            offspring(i.familyMembers[3],int(pop.populationSize/pop.families*0.10), family, fn)
            ball = pop.Ball(i.familyMembers[0].angle, i.familyMembers[0].speed, i.familyMembers[0].color, fn)
            family.append(ball)
            print(len(family))
            newPopulation.append(family)
            print(len(newPopulation))
            fn += 1
        print("Pop length:", len(population))
        pop.population.clear()
        print("Pop length:", len(population))
        pop.population += newPopulation
        # pop.population.clear()
        # pop.population.append(newPopulation)
        print("Pop length:", len(population))




        # pop.final = pop.winners + pop.losers
        # print(pop.final[0].distance, pop.final[0].speed)
        # offspring(pop.final[0],int(pop.populationSize*0.50 - 1))
        # offspring(pop.final[1],int(pop.populationSize*0.20))
        # offspring(pop.final[2],int(pop.populationSize*0.20))
        # offspring(pop.final[3],int(pop.populationSize*0.10))
        # ball = pop.Ball(pop.final[0].initVel, pop.final[0].color)
        # pop.population.append(ball)
        # pop.winners.clear()
        # pop.losers.clear()
        # pop.final.clear()