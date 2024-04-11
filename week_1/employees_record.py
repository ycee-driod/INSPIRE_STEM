# this is a program to manage employees records
# written by : Ian
# date : 21/2/2024

f_name = input("Enter your first name : ")
s_name =  input("Enter your second name : ")
salary = float(input("Enter your salary : "))
bonus = float(input("Enter your bonus : "))
s_1= (salary + bonus)

print("My name is",f_name+s_name)
print("The original salary and bonus is ",s_1)

p = salary
r =float(input("Enter the rate : "))
b =float(input("Enter the bonus change : "))

h = (p + (p * (r / 100)))
n_s =(h + (bonus + b ))
print("My name is",f_name+s_name)
print("the new salary and bonus is",n_s)
  








