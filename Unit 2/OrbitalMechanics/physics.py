from celestialBody import*

dt = 0.001
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
            for i in range(len(list)):
                #print(list[i].recpos.empty())
                acc=forces[i]/list[i].m
                list[i].vec+=acc*dt
                list[i].pos+=list[i].vec*dt
                t+=dt/len(list)
                if t % 0.5 < 0.2:
                    list[i].recpos.put(list[i].pos)
                if (list[i].recpos.qsize() > 2500):
                    list[i].recpos.get()
            if t >= 60:
                run = False
                break