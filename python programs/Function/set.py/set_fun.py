# Set operations in Python
# Define two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
# Union of sets
set_union = set_a | set_b  # or set_a.union(set_b)
print("Union:", set_union)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection of sets
set_intersection = set_a & set_b  # or set_a.intersection(set_b)
print("Intersection:", set_intersection)  # Output: {4, 5}
# Difference of sets
set_difference = set_a - set_b  # or set_a.difference(set_b)
print("Difference:", set_difference)  # Output: {1, 2, 3}   
# Symmetric difference of sets
set_sym_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print("Symmetric Difference:", set_sym_diff)  # Output: {1, 2, 3, 6, 7, 8}
# Subset and Superset
print("Is set_a a subset of set_b?", set_a <= set_b)  # Output: False
print("Is set_b a superset of set_a?", set_b >= set_a)  # Output: False
# Adding and removing elements from a set
set_a.add(6)  # Adds 6 to set_a
set_b.remove(4)  # Removes 4 from set_b
print("Set_a after adding 6:", set_a)  # Output: {1, 2, 3, 4, 5, 6}
print("Set_b after removing 4:", set_b)  # Output: {5, 6, 7, 8}
# Set comprehension
squared_set = {x**2 for x in range(1, 6)}
print("Squared Set:", squared_set)  # Output: {1, 4, 9, 16, 25} 
# Frozenset (immutable set)
frozen_set = frozenset([1, 2, 3, 4, 5])
print("Frozenset:", frozen_set)  # Output: frozenset({1, 2, 3, 4, 5})   
# Set membership
print("Is 3 in set_a?", 3 in set_a)  # Output: True
print("Is 4 in set_b?", 4 in set_b)  # Output: False
# Set length
print("Length of set_a:", len(set_a))  # Output: 6
print("Length of set_b:", len(set_b))  # Output: 4  
# Clearing a set
set_a.clear()  # Removes all elements from set_a
print("Set_a after clearing:", set_a)  # Output: set()
# Copying a set
set_c = set_b.copy()  # Creates a copy of set_b and assigns it to set_c
print("Set_c (copy of set_b):", set_c)  # Output: {5, 6, 7, 8}
# Set operations with frozenset
frozen_set_b = frozenset([5, 6, 7, 8])
print("Union of frozen_set and frozen_set_b:", frozen_set | frozen_set_b)  # Output: frozenset({1, 2, 3, 4, 5, 6, 7, 8})
# Intersection of frozen_set and frozen_set_b
print("Intersection of frozen_set and frozen_set_b:", frozen_set & frozen_set_b)  # Output: frozenset({5})
# Symmetric difference of frozen_set and frozen_set_b
print("Symmetric Difference of frozen_set and frozen_set_b:", frozen_set ^ frozen_set_b)  # Output: frozenset({1, 2, 3, 4, 6, 7, 8})
# Set operations with mixed types
mixed_set = {1, "two", 3.0, (4, 5), frozenset({6, 7})}
print("Mixed Set:", mixed_set)  # Output: {1, 'two', 3.0, (4, 5), frozenset({6, 7})}
# Set operations with mixed types
print("Is 'two' in mixed_set?", "two" in mixed_set)  # Output: True
print("Is (4, 5) in mixed_set?", (4, 5) in mixed_set)  # Output: True
print("Is frozenset({6, 7}) in mixed_set?", frozenset({6, 7}) in mixed_set)  # Output: True
# Set operations with mixed types
print("Is 3.0 in mixed_set?", 3.0 in mixed_set)  # Output: True
print("Is 8 in mixed_set?", 8 in mixed_set)  # Output: False
# Set operations with mixed types
print("Is 1 in mixed_set?", 1 in mixed_set)  # Output: True
print("Is 1.0 in mixed_set?", 1.0 in mixed_set) # Output: True (because 1 and 1.0 are considered equal in Python)
# Set operations with mixed types
print("Is 1 in set_a?", 1 in set_a)  # Output: False (because set_a was cleared earlier)
print("Is 1 in set_b?", 1 in set_b)  # Output: False (because 1 is not in set_b)
# Set operations with mixed types
print("Is 1 in frozen_set?", 1 in frozen_set)  # Output: True
print("Is 1 in frozen_set_b?", 1 in frozen_set_b)  # Output: False (because 1 is not in frozen_set_b)   