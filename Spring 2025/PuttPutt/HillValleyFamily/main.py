import graphics as gx
import physics as px
from pop import population
from pop import losers
from pop import winners
import pop
import genetics as gen


gx.setup(600,800)
gx.background()

while gx.VIEW:

    gx.render()
    gx.check_interactions()
    for i in population:
        #if isinstance(i, pop.Family) or isinstance(i, ):
            print("Hello")
            for j in i.familyMembers:
                px.move(j,20)
            gen.next_gen() 