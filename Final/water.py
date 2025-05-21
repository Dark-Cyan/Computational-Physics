from vectors import Vec

ponds = []

class Water:
    def __init__(self, position, radius):
        self.pos = position
        self.r = radius
        self.color = [78, 165, 181]
        ponds.append(self)

pond1 = Water(Vec(-3,-3,0), 2)
pond2 = Water(Vec(3,3,0), 2)