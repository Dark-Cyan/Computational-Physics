import graphics as gx
import physics as px
import golfBall
import math
import genetics as gen  

gx.setup(550,800)
gx.background()

while gx.VIEW:

    gx.render()
    gx.check_interactions()
    for i in golfBall.population:
        px.move(i, 10)#px.move(i,50)
        gen.next_gen() 
    px.timer += px.dt * 50 * 250/200 
         