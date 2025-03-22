import math

class Vector:
    # Default constructor
    def __init__(self, e0=0.0, e1=0.0, e2=0.0):
        self.e = [e0, e1, e2]

    def __getitem__(self, i):
        return self.e[i]

    def x(self):
        return self.e[0]
    
    def y(self):
        return self.e[1]
    
    def z(self):
        return self.e[2]

    def __setitem__(self, i, value):
        self.e[i] = value
    
    # Overriding negation
    def __neg__(self):
        return Vector(-self.e[0], -self.e[1], -self.e[2])
    
    # Overriding addition 
    def __iadd__(self, v):
        self.e[0] += v.e[0]
        self.e[1] += v.e[1]
        self.e[2] += v.e[2]
        return self
    
    # Overriding multiplication
    def __imul__(self, t: float):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self  

    # Overriding division
    def __itruediv__(self, t: float):
        return self.__imul__(1 / t) 
    
    def length_squared(self):
        return (self.e[0] ** 2) + (self.e[1] ** 2) + (self.e[2] ** 2)
    
    def length(self):
        return math.sqrt(length_squared(self))

    # Overriding print
    def __repr__(self):
        return f"Vector({self.e[0]}, {self.e[1]}, {self.e[2]})"
    
# Utility Functions

def Vector_add(u, v):
    return Vector(u.e[0] + v.e[0], u.e[1] + v.e[1], u.e[2] + v.e[2])

def Vector_sub(u, v):
    return Vector(u.e[0] - v.e[0], u.e[1] - v.e[1], u.e[2] - v.e[2])

def Vector_mul(u, v):
    return Vector(u.e[0] * v.e[0], u.e[1] * v.e[1], u.e[2] * v.e[2])

def Vector_scalar_mul(t, v):
    return Vector(t * v.e[0], t * v.e[1], t * v.e[2])

def Vector_scalar_div(v, t):
    return Vector_scalar_mul(1 / t, v)

def dot(u, v):
    return u.e[0] * v.e[0] + u.e[1] * v.e[1] + u.e[2] * v.e[2]

def cross(u, v):
    return Vector(
        u.e[1] * v.e[2] - u.e[2] * v.e[1],
        u.e[2] * v.e[0] - u.e[0] * v.e[2],
        u.e[0] * v.e[1] - u.e[1] * v.e[0]
    )

def unit_vector(v):
    return Vector_scalar_div(v, v.length())