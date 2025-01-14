from celestialBody import*
import itertools

dt = 10000
G = 6.67e-11
t = 0

run = True
go = False

def netForce(list):
    forces = []
    for i in range(len(list)):
        magnitude = Vec(0,0,0)
        for j in range(len(list)):
            if j == i:
                continue
            r = list[j].pos - list[i].pos
            if r == 0:
                magnitude = magnitude
            else:
                magnitude = magnitude + ((G*list[i].m*list[j].m)/(abs(r)**2)) * r.norm()
        forces.append(magnitude)
    return forces

def move(list,reps):
    
    global t
    global run

    withoutSun = []
    for i in list:
        withoutSun.append(i)
    withoutSun.pop(0)

    if go == True:
        for j in range(reps):
            forces = netForce(list)
            t+=dt
            for i in range(len(list)):
                acc=forces[i]/list[i].m
                list[i].vec+=acc*dt
                list[i].pos+=list[i].vec*dt
                
                list[i].correctAngle()

                totalComparisons = 0
                workingMatches = 0
                for a, b in itertools.combinations(withoutSun, 2):
                    totalComparisons += 1
                    if (abs(b.angle - a.angle) <= 20 or abs(b.angle - a.angle) >= 340):
                        workingMatches += 1
                
                if (totalComparisons == workingMatches):
                    years = int(t/60/60/24/365)
                    days = t/60/60/24 - 365*years
                    print ("Years:", years, "Days:", days)
                    run = False
                    break
                
                #if (list[9].angle>= 360 and t >= 60 * 60 * 24 * 30):
                    
            if run == False:
                break