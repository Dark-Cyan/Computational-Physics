import graphics as gx
import physics as px
from pop import ball

gx.setup(600,800)
gx.background()

while gx.VIEW:

    gx.render()
    gx.check_interactions()
    px.move(ball,20)