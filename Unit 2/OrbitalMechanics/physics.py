from celestialBody import*

dt = 0.001
G = 6.67e-11
t = 0

mass = (10000, 10000)
radius = (100, 100)

angle = (0, 0)
speed = (0, 0)

startX = (0, 100)
startY = (0, 100)
start = (Vec(startX[0], startY[0], 0), Vec(startX[1], startY[1], 0))

planets = []
for i in range(len(mass)):
    planet = celestialBody(mass[i],radius[i],start[i],speed[i],angle[i])
    planets.append(planet)

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
            magnitude += ((G*list[i].m*list[i+1])/(abs(r)**2)) * r.norm()
        forces.append(magnitude)
    return forces

def move(list,reps):
    global run
    if go == True:
        for j in range(reps):
            forces = netForce(list)
            for i in range(len(list)):
                acc=forces[i]/list[i].m
                list[i].vec+=acc*dt
                list[i].pos+=list[i].vec*dt
                t+=dt/range(len(list))
                if t == 60:
                    run = False
                if run == False:
                    break