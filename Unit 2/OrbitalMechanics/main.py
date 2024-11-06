import physics
import graphics as gx

gx.setup(800,600)
gx.background()
while physics.run:

    gx.check_interactions()
    gx.frameRate(100)

    physics.move(physics.planets,20)
    gx.render(physics.planets)
    print(f'Distance = {physics.planets[0].pos.x} m')

gx.pg.quit()