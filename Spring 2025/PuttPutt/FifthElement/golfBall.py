from vectors import Vec

class Ball:
    def __init__(self, velocity):
        #Positional Variables
        self.position = Vec(2.75, 0.25, 0)
        self.velocity = velocity
        self.initialVelocity = velocity
        self.acceleration = Vec(0, 0, 0)
        
        #Matter Variables
        self.radius = 0.021335
        self.mass = 0.045

        #Graphical Variables
        self.color = (255, 255, 255)
        self.visible = True

ball = Ball(Vec(0.3,7.5,0))