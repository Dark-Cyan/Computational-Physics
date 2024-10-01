import math
import sys
import os

dap = 10
radius = 0.25
time = 0
pos1 = -dap + radius
pos2 = 0 - radius
vel1 = 4.5
vel2 = -3.2
acc1 = 10
acc2 = -1.56
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
    elif vel1 < 0 and vel2 > 0:
        run = False
        print("No Collision")

sys.exit()