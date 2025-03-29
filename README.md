# ToRaytracingAndBeyond
- Don't remember why this in Sphere.py: 
root = (h - sqrtd) / a
        if (not ray_t.surrounds(root)):
            root = (h + sqrtd) / a
            if (not ray_t.surrounds(root)):
                return False  # No valid intersection