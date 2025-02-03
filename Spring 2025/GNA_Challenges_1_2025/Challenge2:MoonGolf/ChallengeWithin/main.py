import graphics_proj as gx
import physics as px
import genetics as ge
import sys

gx.setup(800, 600)

while gx.view:
    gx.render()
    gx.check_interactions()
    if gx.run:
        px.move(30) 