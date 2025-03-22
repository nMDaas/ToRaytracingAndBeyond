from Vector import Vector
from Color import write_color

# Image

image_width = 255
image_height = 255

# Render

with open("raytracerOutput/output.ppm", "w") as file:
    file.write("P3\n" + str(image_width) + " " + str(image_height) + "\n255\n")

for i in range(0, image_height):
    print("\rScanlines remaining: " + str(image_height - i))
    for j in range(0, image_width):
        pixel_color = Vector((j)/(image_width-1), (i)/(image_height-1), 0)
        write_color(pixel_color)

print("\rDone")