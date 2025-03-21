# Image

image_width = 255
image_height = 255

# Render

with open("raytracerOutput/output.ppm", "w") as file:
    file.write("P3\n" + str(image_width) + " " + str(image_height) + "\n255\n")

for i in range(0, image_height):
    print("\rScanlines remaining: " + str(image_height - i))
    for j in range(0, image_width):
        r = j / (image_width-1)
        g = i / (image_height-1)
        b = 0.0

        ir = int(255.999 * r)
        ig = int(255.999 * g)
        ib = int(255.999 * b)

        with open("raytracerOutput/output.ppm", "a") as file:
            file.write(str(ir) + " " + str(ig) + " " + str(ib) + "\n")

print("\rDone")