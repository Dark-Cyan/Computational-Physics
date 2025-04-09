#fitness algorithm

import golfBall
import random
from vectors import*
from operator import attrgetter
import physics
import time

standarddeviation = 1
threshhold = False

def offspring(a, n):
    #I want "n" offspring of object "a"
    for i in range(n):
        ball = golfBall.Ball(Vec(random.gauss(a.initialVelocity.x, standarddeviation),random.gauss(a.initialVelocity.y, standarddeviation),0), a.color)
        golfBall.population.append(ball)

def next_gen():
    global standarddeviation
    global threshhold
    if len(golfBall.winners) + len(golfBall.losers)==golfBall.populationSize:
        golfBall.population.clear()
        golfBall.winners.sort(key = (attrgetter('score')), reverse = True)
        golfBall.losers.sort(key = (attrgetter('score')), reverse = True)
        golfBall.final = golfBall.winners + golfBall.losers
        print(golfBall.final[0].score, golfBall.final[0].initialVelocity)
        offspring(golfBall.final[0],int(golfBall.populationSize*0.50 - 1))
        offspring(golfBall.final[1],int(golfBall.populationSize*0.20))
        offspring(golfBall.final[2],int(golfBall.populationSize*0.20))
        offspring(golfBall.final[3],int(golfBall.populationSize*0.10))
        ball = golfBall.Ball(golfBall.final[0].initialVelocity, golfBall.final[0].color)
        golfBall.population.append(ball)
        golfBall.winners.clear()
        golfBall.losers.clear()
        golfBall.final.clear()
        physics.startTime = time.time()