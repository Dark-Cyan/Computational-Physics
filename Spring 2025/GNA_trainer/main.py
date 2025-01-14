import graphics_proj as gx
import physics as px
import genetics as ge

gx.setup(800, 600)

while gx.view:
    gx.render()
    gx.check_interactions()
    if gx.run:
        px.move(5)
    if len(px.pop.launcher) == 0:
        ge.mahoraga()
        break