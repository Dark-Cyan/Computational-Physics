import graphics as gx
import physics as px
import pop
 
gx.setup(600,800)
gx.background()

while gx.VIEW:

    gx.render()
    gx.check_interactions()
    px.update(pop.ball,0.0001)  
    print(pop.ball.newPos)