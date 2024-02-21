# This is a program to calculate the volume of a sphere
# Date 20/02/2024
# Written by: Scyther
# A = P(1+0.01r)^n

import math

# P is the princial, the initial amount paid
P = float(input ("Enter Principal"))
# r is the rate in percentage
r = float(input ("Enter rate in percentage"))
# n is the duration in months
n = float(input ("Enter duration to pay back"))

# A is the total amount to be paid back
A = P*((1+(0.01*r))**n)

print("Total hire urchase amount is equal to" + str(A))