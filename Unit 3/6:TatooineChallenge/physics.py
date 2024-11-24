from celestialBody import*

dt = 1000
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
            #newDT(list,9)
            #if list[2].pos.mag() == 215639000000 or list[2].pos.mag() == 184983751434.06757: #215639000000
                #celestialBody(1,25,(list[2].pos + Vec(6400000, 0, 0)), Vec(0,0,0), (255,255,255), "Water Bottle")
                #print(list[len(list)-1].vec)
                #print(list[len(list)-1].pos-list[2].pos)
                #celestialBody(1,25,(list[2].pos + Vec(-6400000, 0, 0)), Vec(0,0,0), (255,255,255), "Water Bottle")
                #print(list[len(list)-1].vec)
                #print(list[len(list)-1].pos-list[2].pos)
                
            if t == 17985000:
                celestialBody(1,25,(list[2].pos + list[2].pos.norm()*6400000), Vec(0,0,0), (255,255,255), "Water Bottle")
                celestialBody(1,25,(list[2].pos - list[2].pos.norm()*6400000), Vec(0,0,0), (255,255,255), "Water Bottle")

            forces = netForce(list)

            while len(list) >= 4:
                print(f'Newtons: {abs(abs(forces[len(list)-1]) - abs(forces[len(list)-2]))} N')
                print(f'Newtons: {forces[len(list)-1]} N')
                print(f'Newtons: {forces[len(list)-2]} N')
                del list[len(list)-1]
                del list[len(list)-1]
            t+=dt
            for i in range(len(list)):
                acc=forces[i]/list[i].m
                list[i].vec+=acc*dt
                list[i].pos+=list[i].vec*dt
                
                if list[2].pos.mag() >= list[2].maxDistance:
                    list[2].maxDistance = list[2].pos.mag()
                elif list[2].pos.mag() <= list[2].minDistance:
                    list[2].minDistance = list[2].pos.mag()
                
                

                list[i].correctAngle()
                if (list[2].angle>= 360 and t >= 60 * 60 * 24 * 30):
                    years = int(t/60/60/24/365)
                    days = t/60/60/24 - 365*years
                    print ("Years:", years, "Days:", days)
                    run = False
                    break
                if (t%(dt*500)<dt*250):
                    list[i].recpos.put(list[i].pos)
                if (list[i].recpos.qsize() > 2500):
                    list[i].recpos.get()
            if run == False:
                break