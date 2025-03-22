from Vector import Vector

def write_color(pixel_color: Vector):
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # Translate the [0,1] component values to the byte range [0,255].
    rbyte = int(255.999 * r)
    gbyte = int(255.999 * g)
    bbyte = int(255.999 * b)

    # Write out the pixel color components.
    with open("raytracerOutput/output.ppm", "a") as file:
        file.write(str(rbyte) + " " + str(gbyte) + " " + str(bbyte) + "\n")