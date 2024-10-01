import math
import sys
import os

time = 0
pos = 4.5
vel = 4.23
acc = -9.8
dt = 0.001
run = True
target = 0
maxHeight = 0

while run:
    pos += dt * vel
    vel += acc * dt
    time += dt
    if pos >= maxHeight:
        maxHeight = pos
    print("Max Height", maxHeight, " m \t Time:", time, " s")

    if pos<target:
        run = False

sys.exit()