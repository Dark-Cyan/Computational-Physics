from stuff import*

g = Vec(0,-9.8,0)
t=0
dt=0.1

def weight(a):
    return a.m*g

def netForce(list):
    forces = []
    for i in range(len(list)):
        if list[i].anchor:
            forces.append(0)
            continue
        magnitude = list[i].grav
        for j in range(len(list)):
            if j == i:
                continue
            r = list[j].pos - list[i].pos
            if r == 0:
                magnitude = magnitude
            elif abs(r) <= list[i].r + list[j].r:
                A = ((list[j].pos-list[i].pos).norm())
                magnitude = magnitude + 6*(A * A.dot(list[i].pos))
        forces.append(magnitude)
    return forces

def move(list, reps):
    global t
    global run

    for i in range(reps):
        for j in range(reps):
            forces = netForce(list)
            t+=dt
            for i in range(len(list)):
                acc=forces[i]/list[i].m
                list[i].vel+=acc*dt
                if list[i].pos.y <= 0:
                    continue
                list[i].pos+=list[i].vel*dt