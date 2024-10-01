import math

class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z
        
def __add__(self, v):
    if isinstance(v, vector):
        return vector((self.x + v.x), (self.y + v.y), (self.z + v.z))
    raise TypeError(f"Cannot add vector with {type(v)}")

def __sub__(self, v):
    if isinstance(v, vector):
        return vector((self.x - v.x), (self.y - v.y), (self.z - v.z))
    raise TypeError(f"Cannot subtract vector with {type(v)}")

def __mul__(self, s):
    if isinstance(s, (int, float)):
        return vector((self.x * s), (self.y * s), (self.z * s))
    else:
        try: 
            return NotImplemented
        except:
            raise TypeError(f"Cannot multiply vector with {type(s)}")

def __rmul__(self, s):
    return self.__mul__(s)

def __truediv__(self, s):
    if isinstance(s, (int, float)):
        return vector((self.x / s), (self.y / s), (self.z / s))
    else:
        try:
            return NotImplemented
        except:
            raise TypeError(f"Cannot divide vector with {type(s)}")

def __rtruediv__(self, s):
    return self.__truediv__(s)

def magnitude(self):
     return math.sqrt((self.x**2) + (self.y**2) + (self.z**2))

def normalize(self):
    m = magnitude(self)
    return vector((self.x / m), (self.y / m), (self.z / m))

#
def dotProduct(self, v):
    return (self.x * v.x) + (self.y * v.y) + (self.z * v.z)

def crossProduct(self, v):
    return vector(((self.y * v.z)-(self.z * v.y)), ((self.z * v.x)-(self.x * v.z)), ((self.x * v.y)-(self.y * v.x)))

def __repr__(self):
    return f"The Vecor = ({self.x},{self.y},{self.z})"