#fitness algorithm

import pop
import random

def sorter():
    if pop.lander == pop.repeats:
        pop.lander.sort(key = lambda f: f.range, reverse=True)

def offspring(a, n):
    #I want "n" offspring of object "a"
    ball = pop.Ball(random.gauss(a.angle,1))