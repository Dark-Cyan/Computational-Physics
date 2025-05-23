import physics
import graphics as gx

gx.setup(800,600)
gx.background()
while physics.run:

    gx.check_interactions()
    gx.frameRate(30)

    physics.move(physics.planets,1000)
    gx.render(physics.planets)
    
#print(f'Maximum Speed: {physics.planets[10].maxSpeed} m/s')
#print(f'Minimum Speed: {physics.planets[10].minSpeed} m/s')
gx.pg.quit()