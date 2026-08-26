# Day 21

# Write a Python program to find words which are greater than given length k.

def find_words(words, k):
result = []
for i in words:
if len(i) > k:
result.append(i)
return result
# Example usage
word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon"]
k = 5
long_words = find_words(word_list, k)
print(f"Words longer than {k} characters: {long_words}")

# Write a Python program for removing i th character from a string.

def remove_char(input_str, i):
if i < 0 or i >= len(input_str):
print(f"Invalid index {i}. The string remains unchanged.")
return input_str
result_str = input_str[:i] + input_str[i + 1:]
return result_str
input_str = "Hello, wWorld!"
i = 7
new_str = remove_char(input_str, i)
print(f"Original String: {input_str}")
print(f"String after removing {i}th character : {new_str}")

# Write a Python program to split and join a string.

input_str = "Python program to split and join a string"
word_list = input_str.split() 
separator = " " 
output_str = separator.join(word_list)
print("Original String:", input_str)
print("List of split Words:", word_list)
print("Joined String:", output_str)

# Write a Python program to check if a given string is binary string or not.

def is_binary_str(input_str):
for i in input_str:
if i not in '01':
return False 
return True  
input_str = "1001110"
if is_binary_str(input_str):
print(f"'{input_str}' is a binary string.")
else:
print(f"'{input_str}' is not a binary string.")
