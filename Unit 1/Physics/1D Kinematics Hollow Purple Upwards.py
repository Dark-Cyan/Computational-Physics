import math
import sys
import os

radius = 0.25
time = 0
pos1 = 20 + radius
pos2 = 25 - radius
vel1 = -2
vel2 = -6.2
acc1 = -9.8
acc2 = -9.8
dt = 0.001
run = True
target = 0
maxHeight = 0

while run:
    pos1 += dt * vel1
    pos2 += dt * vel2
    vel1 += acc1 * dt
    vel2 += acc2 * dt
    time += dt
    #if pos1 >= maxHeight:
    #    maxHeight = pos
    print("Time:", time, " s \t Final Velocit 1:", vel1, " m/s" + "\t Final Velocit 2:", vel2, " m/s")

    if pos1>=pos2:
        run = False
    elif vel1 < vel2 and acc1 < acc2:
        print("No Collision")
        run = False

sys.exit()