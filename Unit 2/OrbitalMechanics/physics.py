from celestialBody import*

dt = 0.001
G = 6.67e-11
t = 0

mass = (1e14, 1e14, 1e14)
radius = (100, 100, 100)

force = ((0,0,0), (0,0,0), (0,0,0))
velocity = (Vec(0,0,0), Vec(0,0,0), Vec(0,0,0))

startX = (-50, 50, 0)
startY = (0, 0, 7500**0.5)
start = (Vec(startX[0], startY[0], 0), Vec(startX[1], startY[1], 0),  Vec(startX[2], startY[2], 0))

color = ((255,0,0), (0,0,255), (0,255,0))

planets = []
for i in range(len(mass)):
    planet = celestialBody(mass[i],radius[i],start[i], force[i], velocity[i], color[i])
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
                acc=forces[i]/list[i].m
                list[i].vec+=acc*dt
                list[i].pos+=list[i].vec*dt
                t+=dt/len(list)
            if t >= 60:
                run = False
                break