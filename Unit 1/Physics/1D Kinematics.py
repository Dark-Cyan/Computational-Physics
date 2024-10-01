import math
import sys
import os

time = 0
pos = -10
vel = 4.5
acc = 2.5
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
    print("Time:", time, " s \t Final Velocity:", vel, " m/s")

    if pos>=target:
        run = False

sys.exit()