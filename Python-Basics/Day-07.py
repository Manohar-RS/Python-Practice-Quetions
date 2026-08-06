# Prime Numbers
# Day 07

# Write a Python Program to Print all Prime Numbers in an Interval of 1-10

lower = 1
upper = 10
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
if num > 1:
for i in range(2, num):
if (num % i) == 0:
break
else:
print(num)
