from celestialBody import*

dt = 10
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
    if go == True:
        for j in range(reps):
            forces = netForce(list)
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
                if (list[1].angle>= 360 and t >= 60):
                    years = int(t/60/60/24/365)
                    days = t/60/60/24 - 365*years
                    print ("Seconds:", t)
                    print ("End Height:", list[1].pos.mag()-1737.5e3)
                    run = False
                    break
            if run == False:
                break