# Day 18
# List

# Write a Python program to Multiply all numbers in the list.

numbers = [10, 20, 30, 40, 50]
product_of_numbers = 1
for i in numbers:
product_of_numbers *= i
print("Product of elements in the list:", product_of_numbers)

# Write a Python program to find smallest number in a list.

numbers = [30, 10, -45, 5, 20]
minimum = numbers[0]
for i in numbers:
if i < minimum:
minimum = i
print("The smallest number in the list is:", minimum)

# Write a Python program to find largest number in a list.

mbers = [30, 10, -45, 5, 20]
maximum = numbers[0]
for i in numbers:
if i > maximum:
maximum = i
print("The largest number in the list is:", maximum)

# Write a Python program to find second largest number in a list.

numbers = [30, 10, 45, 5, 20]
numbers.sort(reverse=True)
if len(numbers) >= 2:
second_largest = numbers[1]
print("The second largest number in the list is:", second_largest)
else:
print("The list does not contain a second largest number.")
