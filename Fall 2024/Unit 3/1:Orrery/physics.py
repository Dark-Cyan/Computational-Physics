from celestialBody import*

dt = 1000
G = 6.67e-11
t = 0

run = True
go = False

def newDT(list, i):
    global dt
    dt = list[i].distanceFromStart/60000000
    if dt == 0:
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
            t+=dt
            for i in range(len(list)):
                acc=forces[i]/list[i].m
                list[i].vec+=acc*dt
                list[i].pos+=list[i].vec*dt
                list[i].distanceFromStart = math.sqrt((list[i].pos.x - list[i].startPoint.x)**2 + (list[i].pos.y - list[i].startPoint.y)**2 + (list[i].pos.z - list[i].startPoint.z)**2)
                #if dt <= 50 and t >= 3600 * 24 * 30:
                    #years = int(t/60/60/24/365)
                    #days = t/60/60/24 - 365*years
                    #print ("Years:", years, "Days:", days)
                    #run = False
                    #break
                if (t%(dt*500)<dt*250):
                    list[i].recpos.put(list[i].pos)
                if (list[i].recpos.qsize() > 2500):
                    list[i].recpos.get()
            if run == False:
                break