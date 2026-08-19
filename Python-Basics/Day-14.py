# Day 14 
# Calculate Factorial , Body mass index 

# Write a Python Program to Find Factorial of Number Using Recursion.

def recur_factorial(n):
if n == 1:
return n
else:
return n*recur_factorial(n-1)
num = int(input("Enter the number: "))
if num < 0:
print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
print("The factorial of 0 is 1")
else:
print("The factorial of", num, "is", recur_factorial(num))

# Write a Python Program to calculate your Body Mass Index.

def bodymassindex(height, weight):
return round((weight / height**2),2)
h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))
print("Welcome to the BMI calculator.")
bmi = bodymassindex(h, w)
print("Your BMI is: ", bmi)
if bmi <= 18.5:
print("You are underweight.")
elif 18.5 < bmi <= 24.9:
print("Your weight is normal.")
elif 25 < bmi <= 29.29:
print("You are overweight.")
else:
print("You are obese.")
