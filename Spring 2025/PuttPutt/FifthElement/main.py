import graphics as gx

gx.setup(550,800)
gx.background()

while gx.VIEW:

    gx.render()
    gx.check_interactions()
    #px.update(pop.ball,0.0001)  
    #print(pop.ball.newPos)