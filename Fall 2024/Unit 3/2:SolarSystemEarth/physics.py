from celestialBody import*

dt = 100
G = 6.67e-11
t = 0

executed = False
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
    global executed
    global t
    global run
    if go == True:
        for j in range(reps):
            forces = netForce(list)
            t+=dt
            if (abs(list[10].pos - list[0].pos) <= 695700e3):
                print(t)
                print(list[10].vec.mag()) 
                run = False
                break
            for i in range(len(list)):
                acc=forces[i]/list[i].m
                list[i].vec+=acc*dt

                if (list[i].vec.mag() > list[i].maxSpeed):
                    list[i].maxSpeed = list[i].vec.mag()
                elif (list[i].vec.mag() < list[i].minSpeed):
                    list[i].minSpeed = list[i].vec.mag()

                list[i].pos+=list[i].vec*dt
                

                list[i].correctAngle()
                
            if run == False:
                break