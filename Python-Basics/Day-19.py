# Day 19 
# List 

# Write a Python program to find N largest elements from a list.

def find_n_largest_elements(lst, n):
sorted_lst = sorted(lst, reverse=True)
largest_elements = sorted_lst[:n]
return largest_elements
N = int(input("N = " ))
numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34, 
result = find_n_largest_elements(numbers, N)
print(f"The {N} largest elements in the list are:", result)

# Write a Python program to print even numbers in a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers in the list:", even_numbers)

# Write a Python program to print odd numbers in a List.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers in the list:", even_numbers)

# Write a Python program to Remove empty List from List.

list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
filtered_list = [i for i in list_of_lists if i]
print("List after removing empty lists:", filtered_list)
