import graphics as gx
import physics as px
from pop import population
from pop import losers
import genetics as gen


gx.setup(600,800)
gx.background()

while gx.VIEW:

    gx.render()
    gx.check_interactions()
    sum = 0
    for i in population:
        sum += len(i.familyMembers)
        for j in i.familyMembers:
            px.move(j,20)
            gen.next_gen() 
    print(len(population[0].familyMembers))
    print(sum)