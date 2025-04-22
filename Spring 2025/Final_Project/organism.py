from vectors import Vec

class Organism:
    def __init__(self, paternalSet, maternalSet):
        self.paternalSet = paternalSet
        self.maternalSet = maternalSet
        self.position = Vec(0,0,0)
        self.size = 0.3

bacteria = Organism([0,1], [0,0])
organisms = [bacteria]

