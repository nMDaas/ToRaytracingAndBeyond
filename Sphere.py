import math
from Hittable import Hittable, HitRecord
from Vector import Vector, dot
from Ray import Ray

class Sphere(Hittable):
    def __init__(self, center: Vector, radius: float):
        self.center = center
        self.radius = max(0, radius)  # Ensure radius >= 0

    def hit(self, r: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> bool:
        oc = self.center - r.origin()
        a = r.direction().length_squared()
        h = dot(r.direction(), oc)
        c = oc.length_squared() - self.radius * self.radius

        discriminant = h * h - a * c
        if discriminant < 0:
            return False  # No intersection

        sqrtd = math.sqrt(discriminant)

        # Find the nearest root within the acceptable range
        root = (h - sqrtd) / a
        if root <= ray_tmin or ray_tmax <= root:
            root = (h + sqrtd) / a
            if root <= ray_tmin or ray_tmax <= root:
                return False  # No valid intersection

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius # divide by self.radius to make it a unit vector
        rec.set_face_normal(r, outward_normal)

        return True
