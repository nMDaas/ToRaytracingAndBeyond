from typing import List
from Hittable import Hittable, HitRecord
from Ray import Ray
from Interval import Interval

class HittableList(Hittable):
    def __init__(self, object: Hittable = None):
        self.objects: List[Hittable] = []
        if object:
            self.add(object)

    def clear(self):
        """Clears the list of hittable objects."""
        self.objects.clear()

    def add(self, object: Hittable):
        """Adds a hittable object to the list."""
        self.objects.append(object)

    def hit(self, r: Ray, ray_t: Interval, rec: HitRecord) -> bool:
        """Checks if the ray hits any object in the list and updates the closest hit record."""
        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = ray_t.max

        for obj in self.objects:
            if obj.hit(r, Interval(ray_t.min, closest_so_far), temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.t = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal

        return hit_anything
