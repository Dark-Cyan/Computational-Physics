from vectors import Vec
import random

class Organism:
    def __init__(self, paternalSet, maternalSet):
        self.paternalSet = paternalSet
        self.maternalSet = maternalSet
        self.position = Vec(0,0,0)
        self.newPosition = Vec(0,0,0)
        self.size = 0.1
        self.color = (255,255,255)
        self.state = "satisfied"
        self.radius = 1
        self.speed = 0.1

    def update(self):
        dt = 0.1
        if self.state == "satisfied":
            if abs(self.newPosition - self.position) < 0.01:
                self.newPosition = self.position + Vec(random.randrange(-self.radius, self.radius),random.randrange(-self.radius, self.radius),0)
            else:
                self.position += (self.newPosition - self.position).norm() * self.speed * dt

bacteria = Organism([0,1], [0,0])
organisms = [bacteria]