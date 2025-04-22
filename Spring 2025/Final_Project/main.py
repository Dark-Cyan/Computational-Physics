import graphics as gx

gx.setup(1000,1000)
gx.background()

while gx.view:

    gx.render()
    gx.check_interactions() 