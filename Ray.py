from Vector import Vector

class Ray:
    def __init__ (self, origin: Vector, direction: Vector):
        self.orig = origin
        self.dir = direction

    def origin(self):
        return self.orig
    
    def direction(self):
        return self.dir
    
    def at(self, t: float):
        return self.orig + (t * self.dir)