# Day 22
# Dictionary  

# Write a Python program to Extract Unique dictionary values.

my_dict = {
'a': 10,
'b': 20,
'c': 10,
'd': 30,
'e': 20
}
uni_val = set()
for i in my_dict.values():
uni_val.add(i)
unique_values_list = list(uni_val)
print("Unique values in the dictionary:", unique_values_list)

# Write a Python program to find the sum of all items in a dictionary.

my_dict = {
'a': 10,
'b': 20,
'c': 30,
'd': 40,
'e': 50
}
total_sum = 0
for i in my_dict.values():
total_sum += i
print("Sum of all items in the dictionary:", total_sum)

# Write a Python program to Merging two Dictionaries.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print("Merged Dictionary (using update()):", dict1)

# OR

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary (using dictionary unpacking):", merged_dict)

# Write a Python program to convert key-values list to flat dictionary.

key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
flat_dict = {}
for key, value in key_values_list:
flat_dict[key] = value
print("Flat Dictionary:", flat_dict)
