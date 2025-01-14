import math
 
class Ball:
    def __init__(self,mass,radius,pos,vel,dragC):

        self.pos=pos
        self.mass=mass
        self.vel=vel
        self.acc=0
        self.C=dragC
        #self.A=math.pi*radius**2
        self.A=radius
        self.T = 0
        self.P = 0


