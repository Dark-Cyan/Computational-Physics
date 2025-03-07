#fitness algorithm

import pop
from pop import population
import random
from vectors import*
from operator import attrgetter

def offspring(a, n, family, SD, fn):
    #I want "n" offspring of object "a"
    for i in range(n):
        ball = pop.Ball(90, random.gauss(a.speed, SD), a.color, fn)#random.gauss(a.angle, SD),random.gauss(a.speed, SD), a.color, fn)
        family.familyMembers.append(ball)

def lowestHighest(list):
    minAngle = 180
    maxAngle = 180

def next_gen():
    global standarddeviation
    global threshhold
    if pop.finished>=pop.populationSize:
        pop.finished = 0
        newPopulation = []
        # pop.population.clear()
        # pop.lander.sort(key = lambda f: f.range, reverse = True)
        
        # pop.winners.sort(key = (attrgetter('speed')), reverse = False)
        # pop.losers.sort(key = (attrgetter('distance')), reverse = False)
        fn = 0

        # for i in population:
        #     sum = 0
        #     for j in i.familyMembers:
        #         sum+=j.distance
        #     print("VVVVV")
        #     print("Average:", sum/len(i.familyMembers))
        #     print("Past Average:", i.average)
        #     if i.average is None:
        #         i.average = sum/len(i.familyMembers)
        #         continue
        #     if sum/len(i.familyMembers) > i.average:
        #         population.remove(i)
        #         # print("HELLO")
        #     print(sum/len(i.familyMembers))
        #     i.average = sum/len(i.familyMembers)
        # print(len(population))
        # pop.populationSize = len(population)

        

        for i in population:
            i.familyMembers.sort(key = (attrgetter('score')), reverse = False)
            

            #family = pop.Family(pop.populationSize/pop.families,, 1, i)

            family = pop.Family(0, 0, 0, i.standardDeviation * 0.75, fn)
            family.color = i.color
            offspring(i.familyMembers[0],int(pop.populationSize/pop.families*0.50), family, family.standardDeviation, fn)
            offspring(i.familyMembers[1],int(pop.populationSize/pop.families*0.50-1), family, family.standardDeviation, fn)
            ball = pop.Ball(i.familyMembers[0].angle, i.familyMembers[0].speed, i.familyMembers[0].color, fn)
            family.familyMembers.append(ball)
            family.average=i.average
            newPopulation.append(family)
            fn += 1

        bestGroup = 0
        lowAvg = 1000
        bestInd = 0
        bestIndGroup = 0
        indSpeed = 1000
        indDist = 1000

        for i in population:
            average = 0
            count = 0
            for j in i.familyMembers:
                average += j.distance
                if (j.distance < indDist or (j.distance == indDist and j.speed < indSpeed)):
                    bestInd = count
                    bestIndGroup = i.fn
                    indSpeed = j.speed
                    indDist = j.distance
                count += 1
            if (average < lowAvg):
                bestGroup = i.fn
                lowAvg = average
        print("Best Group:", population[bestGroup].color, '\t', "Distance:", lowAvg)
        print("Best Individual:", population[bestIndGroup].familyMembers[bestInd].color, '\t', "Distance:", indDist, '\t', "Speed:", indSpeed, '\t', "Angle:", population[bestIndGroup].familyMembers[bestInd].angle)
        print("__________________________________________________________________________________________")

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