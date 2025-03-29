from Hittable import Hittable, HitRecord
from Vector import Vector, unit_vector
from Interval import Interval
from Ray import Ray
from Color import write_color
from Utility import random_double

class Camera:

    aspect_ratio: float
    image_width: float
    samples_per_pixel: int # Count of random samples for each pixel for antialiasing

    def __init__(self, aspect_ratio=(16.0/9.0), image_width=255, samples_per_pixel=10):
        self.aspect_ratio = aspect_ratio
        self.image_width = image_width
        self.samples_per_pixel = samples_per_pixel

    def render(self, world: Hittable):
        self.initialize()

        with open("raytracerOutput/output.ppm", "w") as file:
            file.write("P3\n" + str(self.image_width) + " " + str(self.image_height) + "\n255\n")

        for i in range(0, self.image_height):
            print("\rScanlines remaining: " + str(self.image_height - i))
            for j in range(0, self.image_width):

                pixel_color = Vector(0,0,0)

                for sample in range(self.samples_per_pixel):
                    r = self.get_ray(j,i)
                    pixel_color += self.ray_color(r, world)

                write_color(self.pixel_samples_scale * pixel_color)

        print("\rDone")

    def initialize(self):
        # Calculate the image height, and ensure that it's at least 1.
        self.image_height = int(self.image_width / self.aspect_ratio)
        self.image_height = 1 if self.image_height < 1 else self.image_height

        self.pixel_samples_scale = 1.0 / self.samples_per_pixel

        focal_length = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * ((self.image_width)/self.image_height)
        self.center = Vector(0, 0, 0)

        # Calculate the vectors across the horizontal and down the vertical viewport edges.
        viewport_u = Vector(viewport_width, 0, 0)
        viewport_v = Vector(0, -viewport_height, 0)

        # Viewport widths less than one are ok since they are real valued.
        viewport_height = 2.0
        viewport_width = viewport_height * (self.image_width/self.image_height)

        # Calculate the horizontal and vertical delta vectors from pixel to pixel.
        self.pixel_delta_u = viewport_u / float(self.image_width)
        self.pixel_delta_v = viewport_v / float(self.image_height)

        # Calculate the location of the upper left pixel.
        viewport_upper_left = self.center - Vector(0, 0, focal_length) - viewport_u/2 - viewport_v/2
        self.pixel00_loc = viewport_upper_left + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)

    def get_ray(self, i: int, j:int):
        # Construct a camera ray originating from the origin and directed at randomly sampled
        # point around the pixel location i, j.

        offset = self.sample_square()
        pixel_sample = self.pixel00_loc + ((i + offset.x()) * self.pixel_delta_u) + ((j + offset.y()) * self.pixel_delta_v)

        ray_origin = self.center
        ray_direction = pixel_sample - ray_origin

        return Ray(ray_origin, ray_direction)

    def sample_square(self):
        # Returns the vector to a random point in the [-.5,-.5]-[+.5,+.5] unit square.
        return Vector(random_double() - 0.5, random_double() - 0.5, 0)

    def ray_color(self, r: Ray, world: Hittable):
        rec = HitRecord()
        if (world.hit(r, Interval(0, float('inf')), rec)):
            return 0.5 * (rec.normal + Vector(1,1,1))

        # If nothing was hit
        unit_direction = unit_vector(r.direction())
        a = 0.5*(unit_direction.y() + 1.0)
        return (1.0-a)*Vector(1.0, 1.0, 1.0) + a*Vector(0.5, 0.7, 1.0)