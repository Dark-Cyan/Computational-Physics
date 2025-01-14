import physics
import graphics as gx

gx.setup(800,600)
gx.background()
while physics.run:

    gx.check_interactions()
    gx.frameRate(1000)

    physics.move(physics.planets,3200)
    gx.render(physics.planets)
    
print(f'Maximum Speed: {physics.planets[1].maxSpeed} m/s')
print(f'Minimum Speed: {physics.planets[1].minSpeed} m/s')
gx.pg.quit()