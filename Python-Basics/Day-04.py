# Topic       : Variables
# Day         : 04

# Write a Python program to swap two variables.

a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")
print(f"Original values: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"Swapped values: a = {a}, b = {b}")
