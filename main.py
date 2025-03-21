# Image

image_width = 256
image_height = 256

# Render

print("P3\n" + str(image_width) + " " + str(image_height) + "\n255\n")

for i in range(0, image_height-1):
    for j in range(0, image_width-1):
        r = i / (image_width-1)
        g = j / (image_height-1)
        b = 0.0

        ir = int(255.999 * r);
        ig = int(255.999 * g);
        ib = int(255.999 * b);

        print(str(ir) + " " + str(ig) + " " + str(ib) + "\n")
        