import physics
import graphics as gx

gx.setup(800,600)
gx.background()
while physics.run:

    gx.check_interactions()
    gx.frameRate(500)
    
    #brute forcing main
    #for i in physics.balls:
        #gx.render(i)
        #physics.move(i,20)

    gx.render(physics.baseball)
    physics.move(physics.baseball,20)

gx.pg.quit()