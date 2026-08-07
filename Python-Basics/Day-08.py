# Factorial Numbers & multiplication Table 
# Day 08

# Write a Python Program to Find the Factorial of a Number.

num = int(input("Enter a number: "))
factorial = 1
if num <0:
print("Factirial does not exist for negative numbers")
elif num == 0:
print("Factorial of 0 is 1")
else:
for i in range(1, num+1):
factorial = factorial*i
print(f'The factorial of {num} is {factorial}')

# Write a Python Program to Display the multiplication Table.

num = int(input("Display multiplication table of: "))
for i in range(1, 11):
print(f"{num} X {i} = {num*i}")
