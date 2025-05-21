import math

class Vec:

    def __init__(self, x, y, z):
        
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def __add__(self,vector):

        if isinstance(vector, Vec):

            return Vec(self.x+vector.x,self.y+vector.y,self.z+vector.z)
    
        else:

            return NotImplemented
            
    def __sub__(self,vector):

        if isinstance(vector, Vec):

            return Vec(self.x-vector.x,self.y-vector.y,self.z-vector.z)
            
        else:

            return NotImplemented
    
    def __mul__(self,scalar):
        
        if isinstance(scalar,(float,int)):

            return Vec(scalar*self.x,scalar*self.y,scalar*self.z)

        else:

            return NotImplemented

    def __rmul__(self,scalar):

        return self*scalar
    
    def __truediv__(self,scalar):

        if isinstance(scalar,(float,int)):

            if scalar == 0:
                raise ZeroDivisionError("Division by zero.")

            return Vec(self.x/scalar,self.y/scalar,self.z/scalar)
        
        else:

            return NotImplemented
            
    def cross(self,vector):

        if isinstance(vector,Vec):
            
            x=(self.y*vector.z)-(self.z*vector.y)
            y=(self.z*vector.x)-(self.x*vector.z)
            z=(self.x*vector.y)-(self.y*vector.x)
        
            return Vec(x,y,z)
        
        else:

            raise TypeError(f"Cannot cross a vector with a(n) {type(vector)}.")
    
    def dot(self,vector):

        if isinstance(vector,Vec):

            return (self.x*vector.x)+(self.y*vector.y)+(self.z*vector.z)
        
        else:

            raise TypeError(f"Cannot dot a vector with a(n) {type(vector)}.")

        
    def __repr__(self):

        return f"Vec({self.x}, {self.y}, {self.z})"
    

    def rot2D(self, theta_degrees):  # This rotates the vector counterclockwise by theta_degrees
        
        rad = math.radians(theta_degrees)
        x_new = self.x * math.cos(rad) - self.y * math.sin(rad)
        y_new = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vec(x_new,y_new,0)


    def mag(self):

        return (self.x**2+self.y**2+self.z**2)**(0.5)
    
    def __abs__(self):

        return self.mag()
    
    def norm(self):

        mag=self.mag()
        if mag==0:
            return Vec(0,0,0)
        
        return (self/mag)
    
    def __eq__(self, vector):

        if isinstance(vector, Vec):

            return self.x == vector.x and self.y == vector.y and self.z == vector.z
        
        return False

