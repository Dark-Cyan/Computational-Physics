import graphics as gx
import physics as px
from pop import population
import pop
import genetics as gen

gx.setup(600,800)
gx.background()

while gx.VIEW:

    gx.render()
    gx.check_interactions()
    count = 0
    for i in population:
        if isinstance(i, pop.Family):
            for j in i.familyMembers:
                px.move(j,20)
            gen.next_gen() 