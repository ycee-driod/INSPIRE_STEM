# Program that deduces the next term in a geometric progression.
# Date: 20/02/2024
# Created by kimathi
# n^th = ar^n-1 
# The n^th term is the number of wtf!!!
#a is the fist term
# n is the number of terms
# r is the common ratio


import math

a = float(input ("Enter first term"))
n = float(input ("Enter number of terms"))
r = float(input ("Enter the common ratio"))

Nth = a*((r)**n-1)

print("N is equal to" + str(Nth))