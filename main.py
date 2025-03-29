from Vector import Vector,dot,unit_vector
from Color import write_color
from Ray import Ray
from Hittable import Hittable, HitRecord
from HittableList import HittableList
from Sphere import Sphere
from Camera import Camera

# World
world = HittableList()
world.add(Sphere(Vector(0,0,-1), 0.5))
world.add(Sphere(Vector(0,-100.5,-1), 100))

aspect_ratio = 16.0 / 9.0
image_width  = 400
samples_per_pixel = 100
cam = Camera(aspect_ratio, image_width, samples_per_pixel)

cam.render(world)