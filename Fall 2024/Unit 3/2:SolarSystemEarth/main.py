import physics
import graphics as gx

gx.setup(800,600)
gx.background()
while physics.run:

    gx.check_interactions()
    gx.frameRate(100)

    physics.move(physics.planets,100)
    gx.render(physics.planets)
    
#print(f'Maximum Speed: {physics.planets[10].maxSpeed} m/s')
#print(f'Minimum Speed: {physics.planets[10].minSpeed} m/s')
gx.pg.quit()