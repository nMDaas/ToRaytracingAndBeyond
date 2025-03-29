from Vector import Vector
from Interval import Interval

def write_color(pixel_color: Vector):
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # Translate the [0,1] component values to the byte range [0,255]
    intensity = Interval(0.000, 0.999)
    rbyte = int(255.999 * intensity.clamp(r))
    gbyte = int(255.999 * intensity.clamp(g))
    bbyte = int(255.999 * intensity.clamp(b))

    # Write out the pixel color components.
    with open("raytracerOutput/output.ppm", "a") as file:
        file.write(str(rbyte) + " " + str(gbyte) + " " + str(bbyte) + "\n")