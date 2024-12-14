from stuff import*

#Time Variables
t = 0
dt = 0.1

#Physics Variables
elasticity = 0

# Constants
COLORS = [
    (245,0,0),
    (250,100,100),
    (150,20,250),
    (250,210,10),
    (250,150,0),
    (245,0,0),
    (250,250,100),
    (255,180,180),
    (255,255,0),
    (100,235,10),
    (0,185,0)
]
RADII = [17,25,32,38,50,63,75,87,100,115,135]
Density = 0.001
POINTS = [1,3,6,10,15,21,28,36,45,55,66]

def weight(a):
    return a.m*a.grav

def handle_fruit_collisions(fruit, list):
    for other_fruit in list:
        if (fruit == other_fruit):
            continue
        dist = other_fruit.pos - fruit.pos
        if dist.mag() <= fruit.r + other_fruit.r:
            fruit.falling = True
            other_fruit.falling = True
            resolve_overlap(fruit, other_fruit)
            if (fruit.type == other_fruit.type):
                list.remove(fruit)
                list.remove(other_fruit)
                newFruit = stuff(Density*math.pi*(RADII[fruit.type+1]**2), RADII[fruit.type+1], Vec((fruit.pos.x+other_fruit.pos.x)/2, (fruit.pos.y+other_fruit.pos.y)/2, 0), Vec(0,0,0), Vec(0,-9.8,0), False, COLORS[fruit.type+1], fruit.type+1)
                continue
            ví = get2DForces(fruit, other_fruit)
            fruit.vel += 2 * ví
            other_fruit.vel += -2 * ví

def resolve_overlap(fruit, other_fruit):
    """
    Moves the balls apart if they are overlapping.
    """
    # Relative position and distance
    relative_position = other_fruit.pos - fruit.pos
    distance = relative_position.mag()
    overlap = fruit.r + other_fruit.r - distance

    if overlap > 0:  # If there's overlap
        # Direction to move the balls apart
        correction = relative_position.norm() * (overlap / 2)
        fruit.pos -= correction
        other_fruit.pos += correction

def get1DForces(fruit, other_fruit):
    ví = (fruit.m * fruit.vel + other_fruit.m * other_fruit.vel - other_fruit.m * elasticity * (fruit.vel - other_fruit.vel))/(fruit.m + other_fruit.m)
    return ví

def get2DForces(fruit, other_fruit):
    relative_position = other_fruit.pos - fruit.pos
    normal = relative_position.norm()

    relative_velocity = other_fruit.vel - fruit.vel
    velocity_along_normal = relative_velocity.dot(normal)
    if velocity_along_normal > 0:
        return Vec(0,0,0)

    v1n = fruit.vel.dot(normal) * normal
    v2n = other_fruit.vel.dot(normal) * normal

    vín = (fruit.m * v1n + other_fruit.m * v2n - other_fruit.m * elasticity * (v1n - v2n))/(fruit.m + other_fruit.m)
    return vín
    

def move(list, reps):
    global t
    t += dt

    for i in range(reps):
        for fruit in list:
            if fruit.anchor:
                continue
            if fruit.pos.y - fruit.r <= -320:
                fruit.pos.y = -320 + fruit.r
                fruit.vel.y = 0
                fruit.vel.x *= 0
            if fruit.pos.x - fruit.r <= -200: 
                fruit.vel.x *= -0.5
                fruit.pos.x = -200+fruit.r
            elif fruit.pos.x + fruit.r >= 200:
                fruit.vel.x *= -1
                fruit.pos.x = 200-fruit.r
            if fruit.vel.mag() >= 50 and fruit.falling:
                  fruit.vel = fruit.vel.norm() * 10

            fruit.acc = weight(fruit)
            handle_fruit_collisions(fruit, list)
            fruit.vel += fruit.acc * dt
            fruit.pos += fruit.vel * dt
            


