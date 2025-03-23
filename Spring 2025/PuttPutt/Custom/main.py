import graphics as gx
import physics as px
import pop
 
gx.setup(600,800)
gx.background()

while gx.VIEW:

    gx.render()
    gx.check_interactions()
    px.move(pop.ball,10) 