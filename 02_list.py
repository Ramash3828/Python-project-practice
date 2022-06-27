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
# print(multi_list)
another_list = ["Apple", " Banana", "Mango", "Cherry", "Apple", "Cherry"]

# print(another_list[0])  # Access the first item

# print(another_list[-1])  # Access the last item

# print(another_list[2:4]) # Access the range in items
# Note: The search will start at index 2 (included) and end at index 4 (not included)

# print(another_list[2:])  # Access defining the index to end
another_list = ["Apple", " Banana", "Mango", "Cherry", "Apple", "Cherry"]
# Apply the if condition in a list
if "Apple" in another_list:
    print("Yes, 'Apple' is in th another_list")

# Change the value of a specific item, refer to the index number:
another_list[1] = "Pineapple"
# print(another_list)

# Insert a new list item, without replacing any of the existing values.
another_list.insert(2, "Orange")
# print(another_list)
# Insert a new list item, without replacing any of the existing values in a last item.

another_list.append("Lichee")
# print(another_list)

# Append elements from another list to current list:
second_list = ["Coconut", "Lemon"]

another_list.extend(second_list)
# print(another_list)


# Remove the specific item in a list:
another_list.remove("Orange")

# Remove the specific item in a list to the specific index:
another_list.pop(1)

# Remove the last item in a list:
another_list.pop()

# Delete the list
second_list = ["Coconut", "Lemon"]
# del second_list
second_list.clear()
print(len(another_list))

# Shorthand for loop
[print(x) for x in another_list]
