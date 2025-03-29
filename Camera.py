from Hittable import Hittable, HitRecord
from Vector import Vector, unit_vector
from Interval import Interval
from Ray import Ray
from Color import write_color

class Camera:

    aspect_ratio: float
    image_width: float

    def __init__(self, aspect_ratio=(16.0/9.0), image_width=255):
        self.aspect_ratio = aspect_ratio
        self.image_width = image_width

    def render(self, world: Hittable):
        self.initialize()

        with open("raytracerOutput/output.ppm", "w") as file:
            file.write("P3\n" + str(self.image_width) + " " + str(self.image_height) + "\n255\n")

        for i in range(0, self.image_height):
            print("\rScanlines remaining: " + str(self.image_height - i))
            for j in range(0, self.image_width):
                pixel_center = self.pixel00_loc + (j * self.pixel_delta_u) + (i * self.pixel_delta_v)
                ray_direction = pixel_center - self.camera_center
                r = Ray(self.camera_center, ray_direction)

                pixel_color = self.ray_color(r, world)

                write_color(pixel_color)

        print("\rDone")

    def initialize(self):
        # Calculate the image height, and ensure that it's at least 1.
        self.image_height = int(self.image_width / self.aspect_ratio)
        self.image_height = 1 if self.image_height < 1 else self.image_height


        focal_length = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * ((self.image_width)/self.image_height)
        self.camera_center = Vector(0, 0, 0)

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
        viewport_upper_left = self.camera_center - Vector(0, 0, focal_length) - viewport_u/2 - viewport_v/2
        self.pixel00_loc = viewport_upper_left + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)



    def ray_color(self, r: Ray, world: Hittable):
        rec = HitRecord()
        if (world.hit(r, Interval(0, float('inf')), rec)):
            return 0.5 * (rec.normal + Vector(1,1,1))

        # If nothing was hit
        unit_direction = unit_vector(r.direction())
        a = 0.5*(unit_direction.y() + 1.0)
        return (1.0-a)*Vector(1.0, 1.0, 1.0) + a*Vector(0.5, 0.7, 1.0)