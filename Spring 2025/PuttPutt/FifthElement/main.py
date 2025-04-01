import graphics as gx
import physics as px
import golfBall
import math

gx.setup(550,800)
gx.background()

while gx.VIEW:

    gx.render()
    gx.check_interactions()
    px.move(golfBall.ball,3)  
    #print(math.degrees(math.atan2(golfBall.ball.velocity.y, golfBall.ball.velocity.x)))