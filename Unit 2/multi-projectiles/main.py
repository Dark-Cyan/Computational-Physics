import physics
import graphics as gx

gx.setup(800,600)
gx.background()
while physics.run:

    gx.check_interactions()
    gx.frameRate(60)
    
    #brute forcing main

    completed = 0
    for i in physics.balls:
        gx.render(i)
        if not i.IDLE:
            physics.move(i,20)
            completed += 1
    if completed == 0:
        physics.run = False
print(f'Average Range = {sum(physics.ranges)/len(physics.ranges)} m')


gx.pg.quit()