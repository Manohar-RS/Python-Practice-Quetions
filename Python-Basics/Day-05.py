# Topic       : Calender / Check Leap Year
# Day         : 05

# Write a Python program to display calendar.

import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
print(cal)


# Write a Python Program to Check Leap Year.

year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
print("{0} is a leap year".format(year))
else:
print("{0} is not a leap year".format(year))
