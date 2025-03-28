from abc import ABC, abstractmethod
from dataclasses import dataclass
from Vector import Vector, dot
from Ray import Ray

@dataclass
class HitRecord:
    p: Vector
    normal: Vector
    t: float
    front_face: bool

    def __init__(self, p=None, normal=None, t=None, front_face=False):
        self.p = p
        self.normal = normal
        self.t = t
        self.front_face = front_face

    def set_face_normal(self, r: Ray, outward_normal: Vector):
        # Sets the hit record normal vector.
        # NOTE: the parameter `outward_normal` is assumed to have unit length.

        front_face = dot(r.direction(), outward_normal) < 0
        self.normal = outward_normal if front_face else -outward_normal

class Hittable(ABC):
    @abstractmethod
    def hit(self, r: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> bool:
        pass