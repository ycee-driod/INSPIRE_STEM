# Program that calculates the surface area of a cylinder
# Date: 20/02/2024
# Created by Scyther
# A=2πrh+2πr2

import math

r = float(input ("Enter radius of the base of the cylinder"))
h = float(input ("Enter vertical height of the cylinder"))

# sa represents Surface Area.
sa = (2*(22/7)*r*h + 2*(22/7)*r**2)

print("Surface Area is equal to" + str(sa))
