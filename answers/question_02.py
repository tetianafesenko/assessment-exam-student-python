"""
Given two strings, create a function that returns the total number of unique characters from the combined string.

Examples:
    count_unique_chars("apple", "play") ➞ 5
    "appleplay" has 5 unique characters:  "a", "e", "l", "p", "y"

    count_unique_chars("sore", "zebra") ➞ 7

    count_unique_chars("a", "soup") ➞ 5

Notes:
 - Careful with empty strings
 - All characters will be lowercase.

"""

string_1 = "apple"
string_2 = "play"
count_unique_chars = string_1 + string_2

s=set(count_unique_chars)
print('Elements:',s)


string_1 = "sore"
string_2 = "zebra"
count_unique_chars = string_1 + string_2

s=set(count_unique_chars)  
l=len(s)  
print('Unique chars:',l)

string_1 = "a"
string_2 = "soup"
count_unique_chars = string_1 + string_2

s=set(count_unique_chars)  
l=len(s)  
print('Unique chars:',l)
    