 # A block if code that run together on a unit

def print_name():
    print("My name is ian kimathi")

# Calling the function
print_name()
print_name()
print_name()


def print_details(name, age, id, gender):
    print("I am {0} , {1}years old, {2}id number, {3}gender")

    print_details("iankimathi", "18", "42052762", "male")


def sum_nums(x,y):
    return x + y
z = sum_nums(10,20)

def prod_num(x,y):
    return x * y
z = prod_num(6,7)
print(z)


def print_odds(first_no, last_no):
    for i in range(first_no, last_no):
        print(i % 2)

print_odds(0,15)  

# ASSIGNMENT
# write a funtion to print all prime numbers btn 1 and 99
# write a funtion to print all squares and cubes frm 1-10
# write a funtion to calculate S.A area cy,cone,cube,sphere.Also volume

# PRIME_NUMBERS
# NAME:Ian kimathi
# Date:29/2/2024
#prime 1-99
  # Python program to display all the prime numbers within an interval

lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 0:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# ALL SQUARES AND CUBES            

#squares
def print_squares(first_no,last_no):
    for i in range(first_no,last_no):
     print(i**2)     
print_squares(1,10) 

print("\t")

#cubes
def print_cubes(first_no,last_no):
    for i in range(first_no,last_no):
     print(i**3)     
print_cubes(1,10) 


#S.A CYLINDER, CONE, SPHERE, CUBE
import math

#1 surface area of cylinder
def values(r,h):
    return math.pi * r**2 * 2 + math.pi * 2*r * h
s1=values(7,21)
print(s1)

#2surface area of cone
def values(r,l):
    return math.pi * r**2  + math.pi *r * l
s2=values(7,21)
print(s2)

#3surface area sphere
def values(r):
    return math.pi * r**2 * 4 
s3=values(21)
print(s3)

#4surface area cube
def values(s):
    return 6*s**2
s4=values(21)
print(s4)


#VOLUME CYLINDER, CONE, SPHERE, CUBE
import math

#1volume of cylinder
def values(r,h):
    return math.pi * r**2 * h
v1=values(7,14)
print(v1)

#2volume of cone
def values(r,h):
    return math.pi * 1/3* r**2 * h
v2=values(7,14)
print(v2)

#3volume of sphere
def values(r,h):
    return math.pi * 4/3* r**3 * h
v3=values(7,14)
print(v3)

#4volume of cube
def values(l,w,h):
    return l * w * h
v4=values(7,14,21)
print(v4)

