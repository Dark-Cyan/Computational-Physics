import graphics as gx
from organism import*
from food import Food
import physics as px
import os

import matplotlib.pyplot as plt

count = 0
foodLoops = 1000
foodNum = 8

gx.setup(1000,1000)
gx.background()
Food.spawnFruit(foodNum)
Food.spawnFruit(foodNum)

while gx.view:
    moves = 20
    if px.run:
        for i in organisms:
            px.move(i, moves)
        count += 1 * moves / 20
        if count >= foodLoops:
            Food.spawnFruit(foodNum)
            count = 0
    gx.render()
    gx.check_interactions() 

plt.plot(range(len(totalOrganisms)), totalOrganisms, label = "Organisms")
plt.plot(range(len(avgSpeeds)), avgSpeeds, label = "Average Speed")
plt.plot(range(len(avgVisions)), avgVisions, label = "Average Vision")
plt.plot(range(len(avgBodySegments)), avgBodySegments, label = "Average Body Segments")
plt.title("Traits vs. Time")
plt.legend()
plt.show()