import graphics as gx
import physics as px
import golfBall
import math

gx.setup(550,800)
gx.background()

while gx.VIEW:

    gx.render()
    gx.check_interactions()
    for i in golfBall.family:
        px.move(i,3)  
    # print(abs(golfBall.ball.velocity)) 