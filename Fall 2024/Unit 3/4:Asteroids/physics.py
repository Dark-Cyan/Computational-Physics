from celestialBody import*

dt = 1000
G = 6.67e-11
t = 0

run = True
go = False

def newDT(list, i):
    global dt
    acc = abs(i/list[10].m)
    dt = 1/(acc*10)
    if dt <= 1:
        dt = 1

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
    if go == True:
        for j in range(reps):
            #newDT(list,9)
            forces = netForce(list)
            #newDT(list,forces[10])
            t+=dt
            for i in range(len(list)):
                acc=forces[i]/list[i].m
                list[i].vec+=acc*dt

                if (list[i].vec.mag() > list[i].maxSpeed):
                    list[i].maxSpeed = list[i].vec.mag()
                elif (list[i].vec.mag() < list[i].minSpeed):
                    list[i].minSpeed = list[i].vec.mag()

                list[i].pos+=list[i].vec*dt
                

                list[i].correctAngle()
                print (abs(list[10].pos - list[1].pos))
                if abs(list[10].pos - list[1].pos) <= 2440e3:
                    years = int(t/60/60/24/365)
                    days = t/60/60/24 - 365*years
                    print ("Years:", years, "Days:", days)
                    run = False
                    break
            if run == False:
                break