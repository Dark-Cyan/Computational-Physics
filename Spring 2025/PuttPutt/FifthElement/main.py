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
    moves = 20
    for i in golfBall.population:
        px.move(i, moves)
        gen.next_gen() 
    px.timer += px.dt * moves * 100 / 20
         
#15500 Vec(0.11923726308062293, 20.815404960917864, 0.0)