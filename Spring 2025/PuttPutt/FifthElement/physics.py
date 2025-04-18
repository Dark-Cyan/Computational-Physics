from vectors import*
import random
import math
import time
import golfBall

run = False
startTime = time.time()

#Constants
dt = 0.001
timer = 0
FRIC=0.025

#Clutter Constants
circleBumperPos = Vec(0, 4, 0)
circleBumperRad = 0.5

HOLE=Vec(0,0.15,0)

def forces(a):
    
    return friction(a) + pinball_slope(a)

def friction(a):
    try: 
        return -1*a.velocity.norm()*FRIC
        #return -1*Vec(0, a.velocity.y, 0).norm()*FRIC
    except ValueError:
        
        return Vec(0, 0, 0)
    
def pinball_slope(a):
    return Vec(0,-0.2,0)

def edges(a):
    if a.position.x > 2.9 - a.radius:
        a.velocity.x *= -1
        a.position.x = 2.9 - a.radius
    if a.position.x < -2.4 + a.radius:
        a.velocity.x *= -1
        a.position.x = -2.4 + a.radius
    if a.position.y < 0.1 + a.radius:
        a.velocity.y *= -1
        a.position.y = 0.1 + a.radius

def collision(a):
    #Circle Bumper 
    if abs(a.position - circleBumperPos) < a.radius + circleBumperRad:
        bounceDirection = (a.position - circleBumperPos).norm()
        #a.velocity = abs(a.velocity) * bounceDirection
        a.velocity = 5.00 * bounceDirection
        a.score += 100
    
    if abs(a.position - Vec(0.25, 5.25, 0)) > 2.65 - a.radius and a.position.y >= 5.25:
        bounceDirection = (Vec(0.25, 5.25, 0) - a.position).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(bounceDirection)) * bounceDirection
        # if a.position.x < -2.4:
        #     a.position.x = -2.4 + a.radius
        # if a.position.x > 2.9:
        #     a.position.x = 2.9 - a.radius

        # a.position.y = float(5.25 + (2.65**2 - (a.position.x - 0.25)**2) ** (1/2) - a.radius)
        # print(a.position)

    if a.position.x <= 0 and a.position.y  - a.radius <= 0.1 - 5/24 * a.position.x:
        wallAngle = Vec(5,24,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle
        a.position.y = 0.1 - 5/24 * a.position.x + a.radius

    if a.position.x > 0 and a.position.x <= 2.4 and a.position.y  - a.radius <= 0.1 + 5/24 * a.position.x:
        wallAngle = Vec(-5,24,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle
        a.position.y = 0.1 + 5/24 * a.position.x + a.radius

    if a.position.x >= 2.4 and a.position.x <= 2.5 and a.position.y <= 6 and a.position.y >= 0:
        a.position -= a.velocity * dt
        a.velocity.x *= -0.98
        if a.position.y - a.radius >= 5.95:
            a.velocity *= -0.98
            a.position.y += a.radius * 2
            a.velocity += Vec(0.1,0.1,0)

    if a.position.x >= -2.0 and a.position.x <= -1.9 and a.position.y <= 2.3 and a.position.y >= 1.3:
        a.position -= a.velocity * dt
        a.velocity.x *= -0.98
        if a.position.y - a.radius >= 2.25:
            a.velocity *= -0.98
            if a.velocity.x <= 0.05:
                a.position.x += 0.1

    if a.position.x >= 1.9 and a.position.x <= 2.0 and a.position.y <= 2.3 and a.position.y >= 1.3:
        a.position -= a.velocity * dt
        a.velocity.x *= -0.98
        if a.position.y - a.radius >= 2.25:
            a.velocity *= -0.98
            if a.velocity.x <= 0.05:
                a.position.x -= 0.1

    if a.position.x <= -0.87 and a.position.x >= -2.0 and a.position.y  - a.radius <= 569/480 - 5/24 * (a.position.x + 0.87) and a.position.y + a.radius >= 569/480 - 0.1 - 5/24 * (a.position.x + 0.87):
        a.position -= a.velocity * dt
        wallAngle = Vec(5,24,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle

    if a.position.x >= 0.87 and a.position.x <= 2.0 and a.position.y  - a.radius <= 569/480 + 5/24 * (a.position.x - 0.87) and a.position.y  + a.radius >= 569/480 - 0.1 + 5/24 * (a.position.x - 0.87):
        a.position -= a.velocity * dt
        wallAngle = Vec(-5,24,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle

    if a.position.x <= -1.4 and a.position.x >= -2.4 and a.position.y - a.radius <= 4 - 1/2 * (a.position.x + 1.4) and a.position.y  + a.radius >= 4:
        wallAngle = Vec(1,2,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle
        a.position.y = 4 - 1/2 * (a.position.x + 1.4) + a.radius
    
    if a.position.x >= 1.4 and a.position.x <= 2.4 and a.position.y - a.radius <= 4 + 1/2 * (a.position.x - 1.4) and a.position.y + a.radius >= 4:
        wallAngle = Vec(-1,2,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle
        a.position.y = 4 + 1/2 * (a.position.x - 1.4) + a.radius

    if a.position.x <= -1.4 and a.position.x >= -2.4 and a.position.y - a.radius < 4 and a.position.y + a.radius >= 4 + 1/2 * (a.position.x + 1.4):
        a.position -= a.velocity * dt
        wallAngle = Vec(1,-2,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle

    if a.position.x >= 1.4 and a.position.x <= 2.4 and a.position.y - a.radius < 4 and a.position.y + a.radius >= 4 - 1/2 * (a.position.x - 1.4):
        a.position -= a.velocity * dt
        wallAngle = Vec(-1,-2,0).norm()
        a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle

    lflipperCenter = Vec(-0.9, 1.4 - 5/24, 0)
    lflipperAngle = math.cos(timer) * math.pi/4

    # Estimate angular velocity (simple numerical derivative)
    lflipperAngle_prev = math.cos(timer - dt) * math.pi/4
    omega = (lflipperAngle - lflipperAngle_prev) / dt  # radians per second

    ltopCornerFlip = Vec(-0.9, 1.4 - 5/24, 0)
    ltopEdgeFlip = Vec(-0.2, 251/240, 0)

    lactTRF = rotate_point(ltopCornerFlip, lflipperCenter, lflipperAngle)
    lactTLF = rotate_point(ltopEdgeFlip, lflipperCenter, lflipperAngle)

    flipperEdge = lactTLF - lactTRF
    edgeDir = flipperEdge.norm()

    # Project ball onto flipper edge to find closest point
    ap = a.position - lactTRF
    proj_len = ap.dot(edgeDir)
    proj_point = lactTRF + edgeDir * proj_len

    if 0 <= proj_len <= flipperEdge.mag():
        dist_vec = a.position - proj_point
        if dist_vec.mag() <= a.radius:
            # Point of collision = proj_point
            n = dist_vec.norm()  # collision normal
            r = proj_point - lflipperCenter  # from rotation center to contact point

            # Flipper velocity at contact point: v = omega × r
            v_flipper = Vec(-omega * r.y, omega * r.x, 0)  # 2D cross product

            v_rel = a.velocity - v_flipper
            vel_along_normal = v_rel.dot(n)

            if vel_along_normal < 0:  # moving toward flipper
                e = 1.1  # coefficient of restitution (bounciness)
                j = -(1 + e) * vel_along_normal * a.mass  # impulse magnitude

                impulse = n * j
                a.velocity += impulse / a.mass  # apply impulse to ball

                # Move ball out of flipper to prevent sticking
                penetration = a.radius - dist_vec.mag()
                a.position += n * penetration

    # lflipperCenter = Vec(-0.95, 1.175, 0) #Vec(-0.9, 1.125, 0)
    # lflipperAngle = math.cos(timer) * math.pi/4
    # ltopCornerFlip = Vec(-0.95, 1.175, 0)
    # lactTLF = Vec((ltopCornerFlip - lflipperCenter).x * math.cos(lflipperAngle) - (ltopCornerFlip - lflipperCenter).y * math.sin(lflipperAngle), (ltopCornerFlip - lflipperCenter).x * math.sin(lflipperAngle) + (ltopCornerFlip - lflipperCenter).y * math.cos(lflipperAngle), 0) + lflipperCenter
    # ltopEdgeFlip = Vec(-0.2, 1.175, 0)
    # lactTRF = Vec((ltopEdgeFlip - lflipperCenter).x * math.cos(lflipperAngle) - (ltopEdgeFlip - lflipperCenter).y * math.sin(lflipperAngle), (ltopEdgeFlip - lflipperCenter).x * math.sin(lflipperAngle) + (ltopCornerFlip - ltopEdgeFlip).y * math.cos(lflipperAngle), 0) + lflipperCenter
    # if a.position.x >= lactTLF.x and a.position.x <= lactTRF.x and a.position.y <= lactTRF.y + (lactTRF.y - lactTLF.y)/(lactTRF.x - lactTLF.x) * (a.position.x - lactTRF.x) and a.position.y >= lactTRF.y - 0.1 + (lactTRF.y - lactTLF.y)/(lactTRF.x - lactTLF.x) * (a.position.x - lactTRF.x):
    #     wallAngle = Vec(lactTRF.x - lactTLF.x,-(lactTRF.y - lactTLF.y),0).norm()
    #     a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle
    #     a.position += a.velocity * dt
    #     print("HUZZ")

    rflipperCenter = Vec(0.9, 1.4 - 5/24, 0)
    rflipperAngle = math.cos(timer) * math.pi/4

    # Estimate angular velocity (simple numerical derivative)
    rflipperAngle_prev = math.cos(timer - dt) * math.pi/4
    omega = (rflipperAngle - rflipperAngle_prev) / dt  # radians per second

    rtopCornerFlip = Vec(0.9, 1.4 - 5/24, 0)
    rtopEdgeFlip = Vec(0.2, 251/240, 0)

    ractTRF = rotate_point(rtopCornerFlip, rflipperCenter, rflipperAngle)
    ractTLF = rotate_point(rtopEdgeFlip, rflipperCenter, rflipperAngle)

    flipperEdge = ractTRF - ractTLF
    edgeDir = flipperEdge.norm()

    # Project ball onto flipper edge to find closest point
    ap = a.position - ractTLF
    proj_len = ap.dot(edgeDir)
    proj_point = ractTLF + edgeDir * proj_len

    if 0 <= proj_len <= flipperEdge.mag():
        dist_vec = a.position - proj_point
        if dist_vec.mag() <= a.radius:
            # Point of collision = proj_point
            n = dist_vec.norm()  # collision normal
            r = proj_point - rflipperCenter  # from rotation center to contact point

            # Flipper velocity at contact point: v = omega × r
            v_flipper = Vec(-omega * r.y, omega * r.x, 0)  # 2D cross product

            v_rel = a.velocity - v_flipper
            vel_along_normal = v_rel.dot(n)

            if vel_along_normal < 0:  # moving toward flipper
                e = 1.1  # coefficient of restitution (bounciness)
                j = -(1 + e) * vel_along_normal * a.mass  # impulse magnitude

                impulse = n * j
                a.velocity += impulse / a.mass  # apply impulse to ball

                # Move ball out of flipper to prevent sticking
                penetration = a.radius - dist_vec.mag()
                a.position += n * penetration

    # rflipperCenter = Vec(0.95, 1.175, 0) #Vec(0.9, 1.125, 0)
    # rflipperAngle = math.cos(timer) * math.pi/4
    # rtopCornerFlip = Vec(0.95, 1.175, 0)
    # ractTRF = Vec((rtopCornerFlip - rflipperCenter).x * math.cos(rflipperAngle) - (rtopCornerFlip - rflipperCenter).y * math.sin(rflipperAngle), (rtopCornerFlip - rflipperCenter).x * math.sin(rflipperAngle) + (rtopCornerFlip - rflipperCenter).y * math.cos(rflipperAngle), 0) + rflipperCenter
    # rtopEdgeFlip = Vec(0.2, 1.175, 0)
    # ractTLF = Vec((rtopEdgeFlip - rflipperCenter).x * math.cos(rflipperAngle) - (rtopEdgeFlip - rflipperCenter).y * math.sin(rflipperAngle), (rtopEdgeFlip - rflipperCenter).x * math.sin(rflipperAngle) + (rtopCornerFlip - rtopEdgeFlip).y * math.cos(rflipperAngle), 0) + rflipperCenter
    # if a.position.x >= ractTLF.x and a.position.x <= ractTRF.x and a.position.y <= ractTLF.y + (ractTRF.y - ractTLF.y)/(ractTRF.x - ractTLF.x) * (a.position.x - ractTLF.x) and a.position.y >= ractTLF.y - 0.1 + (lactTRF.y - lactTLF.y)/(lactTRF.x - lactTLF.x) * (a.position.x - ractTLF.x):
    #     wallAngle = Vec(ractTRF.x - ractTLF.x,-(ractTRF.y - ractTLF.y),0).norm()
    #     a.velocity = a.velocity - 2 * (a.velocity.dot(wallAngle)) * wallAngle
    #     a.position += a.velocity * dt
    #     print("CHUZZ")
    
    hinge_center = Vec(-0.9, 143/120 - 0.05, 0)
    to_ball = a.position - hinge_center
    dist = to_ball.mag()
    if dist < (0.05 + a.radius):
        # Push out
        n = to_ball.norm()
        penetration = (0.05 + a.radius) - dist
        a.position += n * penetration

        # Reflect velocity or just zero it slightly away from hinge
        v_along_n = a.velocity.dot(n)
        if v_along_n < 0:
            a.velocity -= n * (1.5 * v_along_n)

    hinge_center = Vec(0.9, 143/120 - 0.05, 0)
    to_ball = a.position - hinge_center
    dist = to_ball.mag()
    if dist < (0.05 + a.radius):
        # Push out
        n = to_ball.norm()
        penetration = (0.05 + a.radius) - dist
        a.position += n * penetration

        # Reflect velocity or just zero it slightly away from hinge
        v_along_n = a.velocity.dot(n)
        if v_along_n < 0:
            a.velocity -= n * (1.5 * v_along_n)


    
    miniBump1 = Vec(-0.35, 5.65, 0)
    miniBump2 = Vec(0, 6.35, 0)
    miniBump3 = Vec(0.35, 6, 0)
    miniBumpRad = 0.15

    if abs(a.position - miniBump1) < a.radius + miniBumpRad:
        bounceDirection = (a.position - miniBump1).norm()
        #a.velocity = abs(a.velocity) * bounceDirection
        a.velocity = 4.00 * bounceDirection
        a.score += 300
    
    if abs(a.position - miniBump2) < a.radius + miniBumpRad:
        bounceDirection = (a.position - miniBump2).norm()
        #a.velocity = abs(a.velocity) * bounceDirection
        a.velocity = 4.00 * bounceDirection
        a.score += 1000
    
    if abs(a.position - miniBump3) < a.radius + miniBumpRad:
        bounceDirection = (a.position - miniBump3).norm()
        #a.velocity = abs(a.velocity) * bounceDirection
        a.velocity = 4.00 * bounceDirection
        a.score += 500

def rotate_point(p, center, angle):
    rel = p - center
    return Vec(
        rel.x * math.cos(angle) - rel.y * math.sin(angle),
        rel.x * math.sin(angle) + rel.y * math.cos(angle),
        0
    ) + center

def stop(a):

    dist_hole = (a.position - HOLE).mag()
    vmag = a.velocity.mag()
    
    if dist_hole < (0.054 - 0.032 * vmag):
        a.visible=False
        a.pos=HOLE
        golfBall.winners.append(a)
        golfBall.population.remove(a)
        a.run = False

    elif abs(a.velocity.x) < 0.1 and (a.position.y <= 0.2 and a.position.x >= 2.5):
        a.visible = False
        golfBall.losers.append(a)
        golfBall.population.remove(a)
        a.run = False



def move(a,n):
    for i in range(n):
        if run and a.run:
            a.acceleration=forces(a)/a.mass
            a.velocity+=a.acceleration*dt
            a.position+=a.velocity*dt
            edges(a)
            collision(a)
            stop(a)