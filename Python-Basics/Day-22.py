# Day 22
# find uncommon words and duplicates 

# Write a Python program to find uncommon words from two Strings.

def uncommon_words(str1, str2):
words1 = set(str1.split())
words2 = set(str2.split())
uncommon_words_set = words1.symmetric_difference(words2)
uncommon_words_list = list(uncommon_words_set)
return uncommon_words_list
string1 = "This is the first string"
string2 = "This is the second string"
uncommon = uncommon_words(string1, string2)
print("Uncommon words:", uncommon)

# Write a Python program to find all duplicate characters in string.

def find_duplicates(input_str):
char_count = {}
duplicates = []
for i in input_str:
if i in char_count:
char_count[i] += 1
else:
char_count[i] = 1
return duplicates
for i, count in char_count.items():
if count > 1:
duplicates.append(i)
input_string = "piyush sharma"
duplicate_chars = find_duplicates(input_string)
print("Duplicate characters:", duplicate_chars)

