# Define a list
my_list = [1, 2, 3, 4, 5]

# Append(): Adds an element to the end of the list
my_list.append(6)
print(f"After append(6): {my_list}")
# Output: After append(6): [1, 2, 3, 4, 5, 6]

# Extend(): Extends the list by appending elements from another iterable
my_list.extend([7, 8, 9])
print(f"After extend([7, 8, 9]): {my_list}")
# Output: After extend([7, 8, 9]): [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Insert(): Inserts an element at a specified position
my_list.insert(0, 0)
print(f"After insert(0, 0): {my_list}")
# Output: After insert(0, 0): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Remove(): Removes the first occurrence of a specified element
my_list.remove(5)
print(f"After remove(5): {my_list}")
# Output: After remove(5): [0, 1, 2, 3, 4, 6, 7, 8, 9]

# Pop(): Removes and returns the element at a specified position (default is the last element)
popped_element = my_list.pop(4)
print(f"After pop(4) which returned {popped_element}: {my_list}")
# Output: After pop(4) which returned 4: [0, 1, 2, 3, 6, 7, 8, 9]

# Clear(): Removes all elements from the list
my_list.clear()
print(f"After clear(): {my_list}")
# Output: After clear(): []

# Index(): Returns the index of the first occurrence of a specified value
my_list = [1, 2, 3, 4, 5, 4]
index = my_list.index(4)
print(f"Index of 4: {index}")
# Output: Index of 4: 3

# Count(): Returns the number of occurrences of a specified element in the list
count = my_list.count(4)
print(f"Count of 4: {count}")
# Output: Count of 4: 2

# Sort(): Sorts the list in ascending order (in-place)
my_list.sort()
print(f"After sort(): {my_list}")
# Output: After sort(): [1, 2, 3, 4, 4, 5]

# Reverse(): Reverses the elements of the list (in-place)
my_list.reverse()
print(f"After reverse(): {my_list}")
# Output: After reverse(): [5, 4, 4, 3, 2, 1]

# Copy(): Returns a shallow copy of the list
copied_list = my_list.copy()
print(f"Copied list: {copied_list}")
# Output: Copied list: [5, 4, 4, 3, 2, 1]
