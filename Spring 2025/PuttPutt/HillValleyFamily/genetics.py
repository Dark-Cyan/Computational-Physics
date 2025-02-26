#fitness algorithm

import pop
from pop import population
import random
from vectors import*
from operator import attrgetter

standarddeviation = 0.5
threshhold = False

def offspring(a, n, family, fn):
    #I want "n" offspring of object "a"
    for i in range(n):
        ball = pop.Ball(random.gauss(a.angle, standarddeviation),random.gauss(a.speed, standarddeviation), a.color, fn)
        family.familyMembers.append(ball)

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
            sum = 0
            for j in i.familyMembers:
                sum+=j.distance
            print("VVVVV")
            print("Average:", sum/len(i.familyMembers))
            print("Past Average:", i.average)
            if i.average is None:
                i.average = sum/len(i.familyMembers)
                continue
            if sum/len(i.familyMembers) > i.average:
                population.remove(i)
                print("HELLO")
            print(sum/len(i.familyMembers))
            i.average = sum/len(i.familyMembers)

        for i in population:
            i.familyMembers.sort(key = (attrgetter('distance')), reverse = False)
            

            #family = pop.Family(pop.populationSize/pop.families,, 1, i)

            family = pop.Family(0, 0, 0, i.standardDeviation, fn)
            offspring(i.familyMembers[0],int(pop.populationSize/pop.families*0.50), family, fn)
            offspring(i.familyMembers[1],int(pop.populationSize/pop.families*0.50-1), family, fn)
            ball = pop.Ball(i.familyMembers[0].angle, i.familyMembers[0].speed, i.familyMembers[0].color, fn)
            family.familyMembers.append(ball)
            newPopulation.append(family)
            fn += 1
        pop.population.clear()
        pop.population += newPopulation
        # pop.population.clear()
        # pop.population.append(newPopulation)




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