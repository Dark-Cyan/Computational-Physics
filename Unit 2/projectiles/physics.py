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
maxRange = 0

#ball parameters

mass = 0.045
radius = 0.021335

#pumpkin chunkin

#barrelLength = 30.48

#brute forcing part 1

#startAngle = 50
#endAngle = 90
#da = 10

#launch parameters

angle = 12
spin = -240 #negative for backspin positive for topspin
speed = 77 #20-abs(spin) #Basketball off the Gordon Dam#40/math.sin(math.radians(angle/3+35)) #Lunar Golf
height = 0 #barrelLength * math.sin(math.radians(angle)) #Pumpkin Chunkin

#brute forcing part 2

#balls = []
#for i in range(startAngle,endAngle,da):
    #baseball=Ball(mass,radius,Vec(0,height,0),speed,i,spin)
    #balls.append(baseball)


baseball=Ball(mass,radius,Vec(0,height,0),speed,angle,spin)

wind = Vec(0,0,-12)

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

def move(a,reps):
    global t
    if go == True:
        for i in range(reps):
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

    #if abs(a.vec.y)<0.01:
    #    print(f'Max Height = {round(a.pos.y,2)} m')
    if a.pos.y > maxHeight:
        maxHeight = a.pos.y
    if a.pos.y<0: #float and it's checking to see if you've hit the ground
        print(f'Time = {t} s')
        print(f'Range = {a.pos.x} m')
        #print(f'Range = {a.pos.x * 1.09361} yd')
        print(f'Final Speed = {a.vec.mag()} m/s')
        print(f'Max Height = {maxHeight} m')
        run = False