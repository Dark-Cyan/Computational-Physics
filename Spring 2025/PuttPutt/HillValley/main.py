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
    for i in population:
        px.move(i,20)
        gen.next_gen() 