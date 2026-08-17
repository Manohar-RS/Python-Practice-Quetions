# Day 12
# Sum Of Natural Numbers / Decimal to Binary , Octal to Hexadecimal

# Write a Python Program to Find the Sum of Natural Numbers

limit = int(input("Enter the limit: "))
sum = 0
for i in range(1, limit + 1):
sum += i
print("The sum of natural numbers up to", limit, "is:", sum)

# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal

dec_num = int(input('Enter a decimal number: '))
print("The decimal value of", dec_num, "is:")
print(bin(dec_num), "in binary.")
print(oct(dec_num), "in octal.")
print(hex(dec_num), "in hexadecimal.")
