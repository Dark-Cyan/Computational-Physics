import graphics as gx
from organism import organisms

gx.setup(1000,1000)
gx.background()

while gx.view:
    moves = 20
    for i in organisms:
        i.update()
        print(i.position )
    gx.render()
    gx.check_interactions() 