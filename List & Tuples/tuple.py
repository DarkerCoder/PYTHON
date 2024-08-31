# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(f"First element: {my_tuple[0]}")  # Output: First element: 1
print(f"Last element: {my_tuple[-1]}")  # Output: Last element: 5

# Count(): Returns the number of occurrences of a specified element in the tuple
count = my_tuple.count(3)
print(f"Count of 3: {count}")  # Output: Count of 3: 1

# Index(): Returns the index of the first occurrence of a specified value
index = my_tuple.index(4)
print(f"Index of 4: {index}")  # Output: Index of 4: 3

# Concatenation
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print(f"Concatenated tuple: {concatenated_tuple}")  # Output: Concatenated tuple: (1, 2, 3, 4, 5, 6, 7, 8)

# Multiplication
multiplied_tuple = my_tuple * 2
print(f"Multiplied tuple: {multiplied_tuple}")  # Output: Multiplied tuple: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Length of a tuple
print(f"Length of tuple: {len(my_tuple)}")  # Output: Length of tuple: 5

# Iterating over elements
print("Elements of the tuple:")
for item in my_tuple:
    print(item)
# Output:
# Elements of the tuple:
# 1
# 2
# 3
# 4
# 5

# Convert tuple to list
tuple_to_list = list(my_tuple)
print(f"Converted to list: {tuple_to_list}")  # Output: Converted to list: [1, 2, 3, 4, 5]

# Convert list to tuple
list_to_tuple = tuple(tuple_to_list)
print(f"Converted back to tuple: {list_to_tuple}")  # Output: Converted back to tuple: (1, 2, 3, 4, 5)
