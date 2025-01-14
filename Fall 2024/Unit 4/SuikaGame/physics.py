from stuff import*

win = False

#Time Variables
t = 0
dt = 0.01

#Physics Variables
elasticity = 0.0

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

#returns the weight of 
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
                if fruit.type == 10:
                    win = True
                    continue
                list.remove(fruit)
                list.remove(other_fruit)
                newFruit = stuff(Density*math.pi*(RADII[fruit.type+1]**2), RADII[fruit.type+1], Vec((fruit.pos.x+other_fruit.pos.x)/2, (fruit.pos.y+other_fruit.pos.y)/2, 0), Vec(0,0,0), Vec(0,-9.8,0), False, COLORS[fruit.type+1], fruit.type+1)
                continue
            ví1 = get2DForces(fruit, other_fruit)
            fruit.vel += 2 * ví1
            other_fruit.vel -= 2 * ví1

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

#currently deprecated
def get1DForces(fruit, other_fruit):
    ví = (fruit.m * fruit.vel + other_fruit.m * other_fruit.vel - other_fruit.m * elasticity * (fruit.vel - other_fruit.vel))/(fruit.m + other_fruit.m)
    return ví

#returns the final velocity for fruit
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
    
#moves objects in list for reps
def move(list, reps):
    global t
    t += dt

    for i in range(reps):
        for fruit in list:
            if fruit.anchor: #if fruit is anchored, continue
                continue
            if fruit.pos.y - fruit.r <= -320: #if fruit edge is less than bottom bound, set fruit pos to inside the bounds
                fruit.pos.y = -320 + fruit.r
                fruit.vel.y = 0
                fruit.vel.x *= 0
            if fruit.pos.x - fruit.r <= -200:  #if fruit edge is less than left bound, reverse x velocity and place inside the bounds
                fruit.vel.x *= -0.5
                fruit.pos.x = -200+fruit.r
            elif fruit.pos.x + fruit.r >= 200: #if fruit edge is more than right bound, reverse x velocity and place inside the bounds
                fruit.vel.x *= -0.5
                fruit.pos.x = 200-fruit.r
            if fruit.vel.mag() >= 50 and fruit.falling: #if speed is greater than 50 and fruit is done falling, slow it down
                  fruit.vel = fruit.vel.norm() * 10

            #update fruit 
            fruit.acc = weight(fruit)/fruit.m
            handle_fruit_collisions(fruit, list)
            fruit.vel += fruit.acc * dt
            fruit.pos += fruit.vel * dt
            


