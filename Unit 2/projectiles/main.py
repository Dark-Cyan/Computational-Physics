import physics
import graphics as gx

gx.setup(800,600)
gx.background()
while physics.run:

    gx.check_interactions()
    gx.frameRate(42)  
    gx.render(physics.baseball)
    physics.move(physics.baseball,20)

gx.pg.quit()