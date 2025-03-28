from Vector import Vector,dot,unit_vector
from Color import write_color
from Ray import Ray
import math

def hit_sphere(center: Vector, radius: float, r: Ray):
    oc = center - r.origin()
    a = dot(r.direction(), r.direction())
    b = -2.0 * dot(r.direction(), oc)
    c = dot(oc, oc) - radius*radius
    discriminant = b*b - 4*a*c
    
    if (discriminant < 0):
        return -1.0
    else:
        return (-b - math.sqrt(discriminant) ) / (2.0*a)

def ray_color(r: Ray):
    t = hit_sphere(Vector(0,0,-1), 0.5, r)
    if (t > 0.0):
        N = unit_vector(r.at(t) - Vector(0,0,-1))
        return 0.5*Vector(N.x()+1, N.y()+1, N.z()+1)
    
    unit_direction = unit_vector(r.direction())
    a = 0.5*(unit_direction.y() + 1.0)
    return (1.0-a)*Vector(1.0, 1.0, 1.0) + a*Vector(0.5, 0.7, 1.0)

# Image

aspect_ratio = 16.0 / 9.0
image_width = 255

# Calculate the image height, and ensure that it's at least 1.
image_height = int(image_width / aspect_ratio)
image_height = 1 if image_height < 1 else image_height

# Camera 

focal_length = 1.0
viewport_height = 2.0
viewport_width = viewport_height * ((image_width)/image_height)
camera_center = Vector(0, 0, 0)

# Calculate the vectors across the horizontal and down the vertical viewport edges.
viewport_u = Vector(viewport_width, 0, 0)
viewport_v = Vector(0, -viewport_height, 0)

# Viewport widths less than one are ok since they are real valued.
viewport_height = 2.0
viewport_width = viewport_height * (image_width/image_height)

# Calculate the horizontal and vertical delta vectors from pixel to pixel.
pixel_delta_u = viewport_u / float(image_width)
pixel_delta_v = viewport_v / float(image_height)

# Calculate the location of the upper left pixel.
viewport_upper_left = camera_center - Vector(0, 0, focal_length) - viewport_u/2 - viewport_v/2
pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

# Render

with open("raytracerOutput/output.ppm", "w") as file:
    file.write("P3\n" + str(image_width) + " " + str(image_height) + "\n255\n")

for i in range(0, image_height):
    print("\rScanlines remaining: " + str(image_height - i))
    for j in range(0, image_width):
        pixel_center = pixel00_loc + (j * pixel_delta_u) + (i * pixel_delta_v)
        ray_direction = pixel_center - camera_center
        r = Ray(camera_center, ray_direction)

        pixel_color = ray_color(r)

        write_color(pixel_color)

print("\rDone")