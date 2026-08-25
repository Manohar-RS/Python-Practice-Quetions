# Day 20
# List

# Write a Python program to Cloning or Copying a list.

# 1. Using Using the Slice Operator
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]
print(cloned_list)

# 2. Using the list() constructor
original_list = [1, 2, 3, 4, 5]
cloned_list = list(original_list)
print(cloned_list)

# 3. Using List Comprehension
original_list = [1, 2, 3, 4, 5]
cloned_list = [item for item in original_list]
print(cloned_list)

# Write a Python program to Count occurrences of an element in a list.

def count_occurrences(l, element):
count = l.count(element)
return count
my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]
element_to_count = 2
occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} appears {occurrences} times in the list")
