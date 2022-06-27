# Lists are used multiple store in a single variable. Lists are one of 4 built-in types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage. List items are ordered, shangeable, and allow duplicate values. List items are indexed, and start items index is [0]. Lists are created using square brackets:

from __future__ import annotations


my_list = ["Apple", " Banana", "Mango", "Cherry"]
# print(type(my_list))

# Duplicate value in a list
another_list = ["Apple", " Banana", "Mango", "Cherry", "Apple", "Cherry"]
# print(another_list)

# To determine how many items a list has, use the len() function:
another_list = ["Apple", " Banana", "Mango", "Cherry", "Apple", "Cherry"]
# print(len(another_list))

# List can contain different data types:

multi_list = ["Apple", True, 888, False, ("hello", "world"), ]
print(multi_list)
