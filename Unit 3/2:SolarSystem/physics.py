from celestialBody import*

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
    if go == True:
        for j in range(reps):
            forces = netForce(list)
            t+=dt
            for i in range(len(list)):
                acc=forces[i]/list[i].m
                list[i].vec+=acc*dt
                if (list[i].vec.mag()>list[i].maxSpeed):
                    list[i].maxSpeed = list[i].vec.mag()
                elif (list[i].vec.mag()<list[i].minSpeed):
                    list[i].minSpeed = list[i].vec.mag()
                list[i].pos+=list[i].vec*dt
                list[i].distanceFromStart = math.sqrt((list[i].pos.x - list[i].startPoint.x)**2 + (list[i].pos.y - list[i].startPoint.y)**2 + (list[i].pos.z - list[i].startPoint.z)**2)
                if t >= 3600 * 24 * 30687:
                    run = False
                    break
                if (t%(dt*500)<dt*250):
                    list[i].recpos.put(list[i].pos)
                if (list[i].recpos.qsize() > 2500):
                    list[i].recpos.get()
            if run == False:
                break