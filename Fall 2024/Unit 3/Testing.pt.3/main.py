import physics
import graphics as gx

gx.setup(800,600)
gx.background()
while physics.run:

    gx.check_interactions()
    gx.frameRate(60)

    physics.move(physics.planets,100)
    gx.render(physics.planets)
    
print(f'Max Speed: {physics.planets[8].maxSpeed}')
print(f'Min Speed: {physics.planets[8].minSpeed}')
gx.pg.quit()