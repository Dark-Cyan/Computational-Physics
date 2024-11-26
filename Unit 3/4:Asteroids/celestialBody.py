#the celestial bodies
import math
import queue
from vectors import*

planets = []

class celestialBody:

    def __init__(self,mass,radius,initial_pos,velocity,color,name):
        self.m=mass
        self.r=radius
        self.pos=initial_pos
        self.startPoint=initial_pos
        self.distanceFromStart = 0
        self.vec = velocity

        self.maxSpeed = self.vec.mag()
        self.minSpeed = self.vec.mag()

        #self.recpos = queue.Queue(0)
        #self.recpos.put(self.pos)
        self.color = color
        self.name = name
        self.orbit = "Undefined"
        self.maxDistance = self.pos.mag()
        self.minDistance = self.pos.mag()

        #very unnecessary
        self.initAngle = 0
        self.angle = 0
        self.correctAngle()
        self.initAngle = self.angle
        self.correctAngle()

        planets.append(self)

    def correctAngle(planet):
        if planet.pos.y>= 0:
            radians = math.atan2(planet.pos.y,planet.pos.x)
        else:
            radians = math.pi * 2 + math.atan2(planet.pos.y,planet.pos.x)
        degrees = math.degrees(radians)
        planet.angle = (degrees - planet.initAngle + 360)%360 + 1

mass = (1988410E24, 3.302E23, 48.685E23, 5.97219E24, 7.349E22, 6.4171E23, 189818722E19, 5.6834E26, 86.813E24, 102.409E24, 2.2E14)
radius = (100, 100, 100, 100, 33, 100, 100, 100, 100, 100, 111)

velocity = (Vec(1.210213161761593E+01, -7.108630163798801, 1.931983570112581E-01), Vec(-2.190221871481897E+04, 4.925311120667249E+04, 6.035452558128558E+03), Vec(3.721667178340711E+03, 3.463984267802168E+04, 2.615937364423928E+02), Vec(-2.721938833676917E+04, 1.301001220575709E+04, 2.722342885856932E-01), Vec(-2.712730958752836E+04, 1.205134830084109E+04, -8.578237996082372E+01), Vec(-2.329101173041912E+04, 1.327344284653195E+03, 5.992829686907538E+02), Vec(-1.276365241375160E+04, 4.020602386913974E+03, 2.688873754486338E+02), Vec(1.433798692571670E+03, 9.435889543208230E+03, -2.209347362177825E+02), Vec(-5.628359829391532E+03, 3.588969078546308E+03, 8.659264543726319E+01), Vec(1.017529896062049E+02, 5.465783969683248E+03, -1.154710529912466E+02), Vec(8.024309821151976E+02, 4.310680197152988E+02, 1.484144220678963E+02))

startX = (-8.954314476268431E+08, 4.800262829038095E+10, 1.070010863072421E+11, 6.412312668699121E+10, 6.372006640390307E+10, -7.930345430607688E+09, 1.970955259843414E+11, 1.410337507081950E+12, 1.677772197233593E+12, 4.468834029236343E+12, -2.947065953655099E+12)
startY = (-7.136648792848191E+08, 1.224636163797745E+10, -1.271206076371771E+10, 1.318457264231664E+11, 1.318043684800627E+11, 2.345644260761537E+11, 7.315556522031220E+11, -2.941281912695686E+11, 2.395865061511429E+12, -1.126093071304762E+11, 4.089719790890038E+12)
startZ = (2.747324307441281E+07, -3.398429932153978E+09, -6.363034972213263E+09, 1.963735964163393E+07, 1.888408624640107E+07, 5.130282017688975E+09, -7.444042333193004E+09, -5.103859514520566E+10, -1.283763416125786E+10, -1.006698149499019E+11, -1.485070694438470E+12)
start = (Vec(startX[0], startY[0], startZ[0]), Vec(startX[1], startY[1], startZ[1]), Vec(startX[2], startY[2], startZ[2]), Vec(startX[3], startY[3], startZ[3]), Vec(startX[4], startY[4], startZ[4]), Vec(startX[5], startY[5], startZ[5]), Vec(startX[6], startY[6], startZ[6]), Vec(startX[7], startY[7], startZ[7]), Vec(startX[8], startY[8], startZ[8]), Vec(startX[9], startY[9], startZ[9]), Vec(startX[10], startY[10], startZ[10]))

color = ((249,215,28), (77, 65, 53), (165,124,27), (107,147,214), (246, 241, 213), (193,68,14), (216,202,157), (227,224,192), (172, 229, 238), (91,93,223), (255, 0, 0))

name = ("Sun", "Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Unknown")

for i in range(len(mass)):
    planet = celestialBody(mass[i],radius[i],start[i], velocity[i], color[i], name[i])
