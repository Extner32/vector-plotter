from math import sqrt

class vec2():
    def __init__(self, x:float=0.0, y:float=0.0) -> None:
        self.x = x
        self.y = y

    def __add__(self, other:"vec2"):
        return vec2(self.x+other.x, self.y+other.y)
    
    
    def __sub__(self, other:"vec2"):
        return vec2(self.x-other.x, self.y-other.y)
    
    def __mul__(self, other):
        if type(other) is float or type(other) is int:
            return vec2(self.x*other, self.y*other)
        elif type(other) is vec2:
            return vec2(self.x*other.x, self.y*other.y)
        
    def __truediv__(self, other):
        if type(other) is float or type(other) is int:
            return vec2(self.x/other, self.y/other)
        elif type(other) is vec2:
            return vec2(self.x/other.x, self.y/other.y)
        
    def __pow__(self, other):
        if type(other) is float or type(other) is int:
            return vec2(self.x**other, self.y**other)
        elif type(other) is vec2:
            return vec2(self.x**other.x, self.y**other.y)
        
    def __str__(self):
        return f"({self.x}, {self.y})"
        
    
    def dot(self, other:"vec2"):
        return self.x*other.x + self.y*other.y
    
    def length(self):
        return sqrt(self.x**2 + self.y**2)
    
    def length_sq(self):
        return self.x**2 + self.y**2
    
    def normalized(self):
        l = self.length()
        if l == 0:
            return vec2(0, 0)
        else:
            return vec2(self.x/l, self.y/l)
        
    
    def to_tup(self):
        return (self.x, self.y)
    
    


