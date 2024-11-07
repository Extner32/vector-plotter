from math import sqrt

class vec3():
    def __init__(self, x:float=0.0, y:float=0.0, z:float=0.0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other:"vec3"):
        return vec3(self.x+other.x, self.y+other.y, self.z+other.z)
    
    
    def __sub__(self, other:"vec3"):
        return vec3(self.x-other.x, self.y-other.y, self.z-other.z)
    
    def __mul__(self, other):
        if type(other) is float or type(other) is int:
            return vec3(self.x*other, self.y*other, self.z*other)
        elif type(other) is vec3:
            return vec3(self.x*other.x, self.y*other.y, self.z*other.z)
        
    def __truediv__(self, other):
        if type(other) is float or type(other) is int:
            return vec3(self.x/other, self.y/other, self.z/other)
        elif type(other) is vec3:
            return vec3(self.x/other.x, self.y/other.y, self.z/other.z)
        
    def __pow__(self, other):
        if type(other) is float or type(other) is int:
            return vec3(self.x**other, self.y**other, self.z**other)
        elif type(other) is vec3:
            return vec3(self.x**other.x, self.y**other.y, self.z**other.z)
        
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
        
    
    def dot(self, other:"vec3"):
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def cross(self, other:"vec3"):
        return vec3(
            #NOT CORRECt!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.z*other.y,
            self.y*other.z - self.z*other.y
        )
    
    def length(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def length_sq(self):
        return self.x**2 + self.y**2 + self.z**2
    
    def normalized(self):
        l = self.length()
        if l == 0:
            return vec3(0, 0, 0)
        else:
            return vec3(self.x/l, self.y/l, self.z/l)
    
    def to_tup(self):
        return (self.x, self.y, self.z)
    
    


