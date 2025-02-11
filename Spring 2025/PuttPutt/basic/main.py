import graphics as gx
import physics as px
from pop import population
from pop import populationSize

gx.setup(600,800)
gx.background()

while gx.VIEW:

    gx.render()
    gx.check_interactions()
    for i in range(populationSize):
        px.move(population[i],20)