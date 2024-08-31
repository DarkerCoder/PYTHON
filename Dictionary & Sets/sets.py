# Create a set
my_set = {1, 2, 3, 4, 5}

# Add elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Remove elements from a set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Check if an element exists in a set
print(2 in my_set)  # Output: True

# Iterate over a set
for element in my_set:
    print(element)

# Get the length of a set
print(len(my_set))  # Output: 5

# Create another set for operations
other_set = {4, 5, 6, 7}

# Union of two sets
union_set = my_set.union(other_set)
print(union_set)  # Output: {1, 2, 4, 5, 6, 7}

# Intersection of two sets
intersection_set = my_set.intersection(other_set)
print(intersection_set)  # Output: {4, 5, 6}

# Difference between two sets
difference_set = my_set.difference(other_set)
print(difference_set)  # Output: {1, 2}

# Check if a set is subset or superset
subset_check = my_set.issubset(other_set)
print(subset_check)  # Output: False

superset_check = my_set.issuperset({1, 2})
print(superset_check)  # Output: True

# Remove all elements from a set
my_set.clear()
print(my_set)  # Output: set()
