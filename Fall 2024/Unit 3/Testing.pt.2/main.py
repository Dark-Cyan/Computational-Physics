import physics
import graphics as gx

gx.setup(800,600)
gx.background()
while physics.run:

    gx.check_interactions()
    gx.frameRate(10000)

    physics.move(physics.planets,4000)
    gx.render(physics.planets)
    
print(f'Max Speed: {physics.planets[10].maxSpeed}')
print(f'Min Speed: {physics.planets[10].minSpeed}')
gx.pg.quit()