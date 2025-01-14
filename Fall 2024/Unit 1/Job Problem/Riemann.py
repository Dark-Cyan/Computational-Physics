# Riemann

import math
import os

#your rate is 0.5*t = rate
#where "t" is in hours
#total made after 100 hours?

time = 0
rate = 0
total = 0
step = 0.000001

os.system("clear")

while time < 100:
    rate = 0.5 * time
    total += rate*step
    time += step
    print("Total Made:", total, "\tTotal Hours:", time)