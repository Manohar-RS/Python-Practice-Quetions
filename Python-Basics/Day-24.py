# Day 24
# OrderedDict()

# Write a Python program to insertion at the beginning in OrderedDict.

from collections import OrderedDict
ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])
new_item = ('a', 1)
new_ordered_dict = OrderedDict([new_item])
new_ordered_dict.update(ordered_dict)
print("Updated OrderedDict:", new_ordered_dict)

# Write a Python program to check order of character in string using OrderedDict().

from collections import OrderedDict
def check_order(string, reference):
string_dict = OrderedDict.fromkeys(string)
reference_dict = OrderedDict.fromkeys(reference)
return string_dict == reference_dict
input_string = "hello world"
reference_string = "helo wrd"
if check_order(input_string, reference_string):
print("The order of characters in the input string matches the reference string")
else:
print("The order of characters in the input string does not match th reference string")


# Write a Python program to sort Python Dictionaries by Key or Value.

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_by_keys = dict(sorted(sample_dict.items()))
print("Sorted by keys:")
for key, value in sorted_dict_by_keys.items():
print(f"{key}: {value}")

# OR

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_by_values = dict(sorted(sample_dict.items(), key=lambda ite
print("Sorted by values:")
for key, value in sorted_dict_by_values.items():
print(f"{key}: {value}")
