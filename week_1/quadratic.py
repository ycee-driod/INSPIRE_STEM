#program to solve the quadratic equation
#date : 20/2/2024
#name : Ian Kimathi
import math

a = float(input("enter the coefficient of the first term"))
b =float(input("enter the coefficient of the second term"))
c = float(input("enter the coeficient of constant : "))


d = float((b)**2) - 4 * (a) * (c)

x_1 = (-b + math.sqrt(d)) / 2*a
x_2 = (-b - math.sqrt(d)) / 2*a

print("the solution of the quadratic equation are :, x_1, x_2")