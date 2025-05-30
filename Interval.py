class Interval:
    min: float
    max: float

    def __init__(self, min=float('inf'), max=-float('inf')):
        self.min = min
        self.max = max

    def size(self):
        return self.max - self.min

    def contains(self, x: float):
        return (self.min <= x) and (x <= self.max)

    def surrounds(self, x: float):
        return (self.min < x) and (x < self.max)
    
    def clamp(self, x: float):
        if (x < self.min): return self.min
        if (x > self.max): return self.max
        return x

# Variables that belong to all instances of Interval
Interval.empty = Interval(float('inf'), -float('inf'))  # Empty interval
Interval.universe = Interval(-float('inf'), float('inf'))