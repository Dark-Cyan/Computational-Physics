from stuff import*

c = 10
g = Vec(0,-9.8,0)
elasticity = 0.5
t=0
dt=0.1

def weight(a):
    return a.m*g

# def checkBall(fruit, fruitList):
#     for other_fruit in fruitList:
#         if fruit == other_fruit:
#             continue
#         r = other_fruit.pos - fruit.pos
#         if abs(r) <= fruit.r + other_fruit.r:
#             R = r.norm()
#             v1n = fruit.vel.dot(R)
#             v2n = other_fruit.vel.dot(-1*R)
#             vin = (fruit.m*v1n+other_fruit.m*v2n-other_fruit.m*elasticity*(v1n-v2n))/(fruit.m+other_fruit.m)
#             a1=vin-v1n
#             aTo = a1.dot(R)
#             fruit.vec = fruit.vec + aTo


# def netForces(list):
#     forces = []
#     for fruit1 in range(len(list)):
#         force = weight(list[fruit1])
#         if list[fruit1].anchor:
#             forces.append(0)
#             continue
#         for fruit2 in range(len(list)):
#             r = list[fruit2].pos - list[fruit1].pos
#             if fruit1 == fruit2:
#                 continue
#             if abs(r) <= list[fruit1].r + list[fruit2].r:
#                 R = r.norm()
#                 v1n = list[fruit1].vel.dot(R) * R
#                 #print("V1n is:", v1n)
#                 v2n = list[fruit2].vel.dot(-1*R) * R

#                 # if (list[fruit2].vel-list[fruit1].vel).dot(list[fruit2].pos-list[fruit1].pos) >= 0:
#                 #     continue
#                 vin = (list[fruit1].m*v1n+list[fruit2].m*v2n-list[fruit2].m*elasticity*(v1n-v2n))/(list[fruit1].m+list[fruit2].m)
#                 print("Vin is:", vin)
#                 a1=vin-v1n
#                 force += a1 * R * list[fruit1].m
# #force+=a1*R*fruit1
#         forces.append(force)
#     return forces
    
#Newton's Laws of Motion
# 1. An object in motion stays in motion
# 2. F = ma
# 3. Each force has an equal and opposite force

# def particleDynamics(list):
#     for i in list:
#         for j in list:
#             if abs(i.pos-j.pos) <= i.r + j.r:
#                 i.vel = i.vel - 2*j.m/(i.m+j.m) * 

def detect_collision(fruit1, fruit2):
    """Detects if two balls have collided."""
    distance = (fruit2.pos - fruit1.pos).mag()
    return distance <= fruit1.r + fruit2.r

def resolve_overlap(fruit1, fruit2):
    """
    Moves the balls apart if they are overlapping.
    """
    # Relative position and distance
    relative_position = fruit2.pos - fruit1.pos
    distance = relative_position.mag()
    overlap = fruit1.r + fruit2.r - distance

    if overlap > 0:  # If there's overlap
        # Direction to move the balls apart
        correction = relative_position.norm() * (overlap / 2)
        fruit1.pos -= correction
        fruit2.pos += correction

def resolve_collision(fruit1, fruit2):
    """Resolves an elastic collision between two balls."""
    # Relative position and velocity
    relative_position = fruit2.pos - fruit1.pos
    relative_velocity = fruit2.vel - fruit1.vel

    # Normal vector (direction of the collision)
    normal = relative_position.norm()

    # Relative velocity in the normal direction
    velocity_along_normal = relative_velocity.dot(normal)

    # If the balls are moving apart, no collision resolution is needed
    if velocity_along_normal > 0:
        return

    # Calculate new velocities using conservation of momentum
    m1, m2 = fruit1.m, fruit2.m
    v1 = fruit1.vel
    v2 = fruit2.vel

    # Compute the impulse scalar
    impulse = 1/8 * -(1 + elasticity) * velocity_along_normal / (1 / m1 + 1 / m2)
    impulse_vector = impulse * normal

    # Update velocities
    fruit1.vel += impulse_vector / m1
    fruit2.vel -= impulse_vector / m2

def move(list, reps):
    global t
    global run

    for j in range(reps):
        t+=dt
        for i in range(len(list)):

            for k in range(len(list)):
                if (i == k):
                    continue
                if detect_collision(list[i],list[k]):
                    print("HELP")
                    resolve_overlap(list[i], list[k])
                    resolve_collision(list[i],list[k])
            forces = weight(list[i])
            acc=forces/list[i].m
            list[i].vel+=acc*dt
            list[i].pos+=list[i].vel*dt
            if list[i].pos.y <= 0:
                list[i].pos.y=0
                list[i].vel.y=0
                list[i].vel.x-=list[i].vel.x/10
            if list[i].pos.x <= -200:
                list[i].vel.x *= -1
            elif list[i].pos.x >= 200:
                list[i].vel.x *= -1
            