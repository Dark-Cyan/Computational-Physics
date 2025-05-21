from vectors import Vec
import random

foods = []

class Food:
    def __init__(self, position, nutrition):
        self.pos = position
        self.nutrition = nutrition
        self.r = 0.03
        self.color = [221, 21, 51]
        foods.append(self)

    def spawnFruit(num):
        for i in range(num):
            newFood = Food(Vec(random.uniform(-5.0, 5.0), random.uniform(-5.0, 5.0), 0), random.uniform(0.1,1))

food1 = Food(Vec(-3,3,0), 0.6)
food2 = Food(Vec(3,-3,0), 0.7)