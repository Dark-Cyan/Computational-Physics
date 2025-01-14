import physics
import graphics as gx

gx.setup(800,600)
gx.background()
while physics.run:

    gx.check_interactions()
    gx.frameRate(10000)

    physics.move(physics.planets,20)
    gx.render(physics.planets)
    #print(f'Distance to Barycenter of System: {physics.planets[2].pos.mag()} m')
    
print(f'Maximum Distance to BaryCenter of System: {physics.planets[2].maxDistance} m')
print(f'Minimum Distance to BaryCenter of System: {physics.planets[2].minDistance} m')
#print(f'Maximum Force on Tatooine: {physics.planets[2].maxForce} N')
gx.pg.quit()