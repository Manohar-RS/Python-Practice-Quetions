# Day 17 

# Write a Python Program to Sort Words in Alphabetic Order.

my_str = input("Enter a string: ")
words = [word.capitalize() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
print(word)

# Write a Python Program to Remove Punctuation From a String.

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = input("Enter a string: ")
no_punct = ""
for char in my_str:
if char not in punctuations:
no_punct = no_punct + char
print(no_punct)

