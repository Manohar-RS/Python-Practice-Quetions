# Day 10
# Armstrong Numbers 

# Write a Python Program to Check Armstrong Number

n = int(input("Enter a number: "))
n_str = str(n)
n_digits = len(n_str)
sum_of_powers = 0
temp_num = n
while temp_num > 0:
digit = temp_num % 10
sum_of_powers += digit ** n_digits
temp_num //= 10
if sum_of_powers == n:
print(f"{n} is an Armstrong number.")
else:
print(f"{n} is not an Armstrong number.")
