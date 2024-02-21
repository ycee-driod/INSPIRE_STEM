# Program that calculates the surface area of a sphere
# Date: 20/02/2024
# Created by ian
# A=4πr^2

import math

r = float(input ("Enter radius of the sphere"))

# sa represents Surface Area.
sa = 4*(22/7)*r**2

print("Surface Area is equal to" + str(sa))