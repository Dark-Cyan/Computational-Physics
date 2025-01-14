#physics engine

from stuff import*

#environmentals

g=Vec(0,-9.8,0) #gravity N/kg
#g=Vec(0,-1.62,0)

p=1.2 #air density
s = 3.5 * 10 ** -5
dt=0.001
t=0

maxHeight = 0
maxHeightTime = 0
maxRange = 0

#ball parameters

mass = 350
radius = 0.4

#pumpkin chunkin

#barrelLength = 30.48

#brute forcing part 1

#startAngle = 50
#endAngle = 90
#da = 10

#launch parameters

angle = 90
spin = 0 #negative for backspin positive for topspin
speed = 2339.2719237 #20-abs(spin) #Basketball off the Gordon Dam#40/math.sin(math.radians(angle/3+35)) #Lunar Golf
height = 0 #barrelLength * math.sin(math.radians(angle)) #Pumpkin Chunkin

#brute forcing part 2

#balls = []
#for i in range(startAngle,endAngle,da):
    #baseball=Ball(mass,radius,Vec(0,height,0),speed,i,spin)
    #balls.append(baseball)


baseball=Ball(mass,radius,Vec(0,height,0),speed,angle,spin)

wind = Vec(0,0,0)

run = True
go = False

def weight(a):
    return a.m*g

def airpseed(a):
    return a.vec - wind

def drag(a):
    return -0.5*a.C*a.A*p*abs(airpseed(a))*airpseed(a)

def netforce(a):
    return weight(a)+drag(a)+lift(a)

def lift(a):
    return s * (a.w.cross(airpseed(a)))

def fixModel(a):
    global p
    h = a.pos.y
    if h < 11000:
        a.T = 15.04 - 0.00649 * h
        a.P = 101.29 * ((a.T + 273.1)/288.08) ** 5.256
    elif h >= 11000 and h < 25000:
        a.T = -56.46
        a.P = 22.65 * math.e ** (1.73 - 0.000157 * h)
    else:
        a.T = -131.21 + 0.00299 * h
        a.P = 2.488 * ((a.T + 273.1)/216.6) ** -11.388
    p = a.P / (0.2869 * (a.T + 273.1))

def move(a,reps):
    global t
    if go == True:
        for i in range(reps):
            fixModel(a)
            acc=netforce(a)/a.m
            a.vec+=acc*dt
            a.pos+=a.vec*dt
            t+=dt
            checker(a)
            if run == False:
                break

def checker(a):
    global run
    global maxHeight
    global maxHeightTime

    #if abs(a.vec.y)<0.01:
    #    print(f'Max Height = {round(a.pos.y,2)} m')
    if a.pos.y > maxHeight:
        maxHeight = a.pos.y
        maxHeightTime = t
    if a.pos.y<0: #float and it's checking to see if you've hit the ground
        print(f'Time = {t} s')
        print(f'Range = {a.pos.x} m')
        #print(f'Range = {a.pos.x * 1.09361} yd')
        print(f'Final Speed = {a.vec.mag()} m/s')
        print(f'Max Height = {maxHeight} m')
        print(f'Max Height Time = {maxHeightTime} s')
        run = False