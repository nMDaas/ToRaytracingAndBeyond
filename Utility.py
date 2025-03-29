import random
import math

def degrees_to_radians(degrees: float):
    return degrees * math.pi / 180.0

def random_double(min: float = 0.0, max: float = 1.0):
    # Returns a random real in [min, max).
    return min + (max - min) * random.random()