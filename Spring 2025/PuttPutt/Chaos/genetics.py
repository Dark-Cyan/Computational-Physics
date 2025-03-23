#fitness algorithm

import pop
import random
from vectors import*
from operator import attrgetter
import physics as phys

newPopulation = []
winners = []    

def next_gen():
    if pop.finished == pop.families + pop.families * pop.children:
        for i in pop.population:
            i.sort(key = (attrgetter('score')), reverse = False)
            if i.familyMembers[0].score==0:
                winners.append(i.familyMembers[0])
                ball=pop.Ball(Vec(random.uniform(-5, 5),random.uniform(0.5, 5), 0), (random.randrange(0,255,1), random.randrange(0,255,1), random.randrange(0,255,1)))
                family = pop.Family(pop.children, ball, 5)
                newPopulation.append(family)
                continue
            standardDeviation = i.familyMembers[0].distance
            family = pop.Family(pop.children, i.familyMembers[0], standardDeviation)
            newPopulation.append(family)

        print("-----------------------------------------------------------------------------")
        print("Current Winners:")
        for i in winners:
            print(i)
        print("-----------------------------------------------------------------------------" + '\n')

        pop.population.clear()
        pop.population += newPopulation
        pop.finished = 0

        newPopulation.clear()