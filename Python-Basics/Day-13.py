# Day 13
# LCM and HCF

# Write a Python Program to Find LCM.

def compute_lcm(x, y):
if x > y:                    
greater = x
else:
greater = y
while(True):
if((greater % x == 0) and (greater % y == 0)):
lcm = greater
break
greater += 1
return lcm
num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The L.C.M. is", compute_lcm(num1, num2))

# Write a Python Program to Find HCF.


def compute_hcf(x, y):
if x > y:
smaller = y
else:
smaller = x
for i in range(1, smaller+1):
if((x % i == 0) and (y % i == 0)):
hcf = i 
return hcf
num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The H.C.F. is", compute_hcf(num1, num2))
