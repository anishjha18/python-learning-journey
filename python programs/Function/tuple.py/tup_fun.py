#tuple functions
tup_1=(1, 2, 3, 4, 5)
tup_2=(6, 7, 8, 9, 10)

#concatenation
tup_3=tup_1+tup_2   #concatenates tup_1 and tup_2 and assigns it to tup_3
print(tup_3)        #prints the concatenated tuple

#repetition
tup_4=tup_1*2       #repeats tup_1 twice and assigns it to tup_4
print(tup_4)        #prints the repeated tuple

#slicing
tup_5=tup_1[2:4]    #slices tup_1 from index 2 to index 3 (4 is exclusive) and assigns it to tup_5
print(tup_5)        #prints the sliced tuple

#length
print(len(tup_1))   #prints the length of tup_1
print(len(tup_2))   #prints the length of tup_2

#membership
print(3 in tup_1)   #checks if the element 3 is present in tup_1 and prints the result (True or False)
print(3 in tup_2)   #checks if the element 3 is present in tup_2 and prints the result (True or False)

#tuple methods
print(max(tup_1))   #finds the maximum value in tup_1 and prints it
print(min(tup_1))   #finds the minimum value in tup_1 and prints it
print(sum(tup_1))   #calculates the sum of all elements in tup_1 and prints it

#tuple indexing
print(tup_1[0])     #prints the first element of tup_1
print(tup_1[-1])    #prints the last element of tup_1

#tuple slicing with step
tup_6=tup_1[::2]   #slices tup_1 with a step of 2, meaning it takes every second element
print(tup_6)        #prints the sliced tuple with step

#tuple reverse
tup_7=tup_1[::-1]  #slices tup_1 with a step of -1, which reverses the tuple
print(tup_7)        #prints the reversed tuple

#tuple unpacking
a, b, c, d, e = tup_1  #unpacks the elements of tup_1 into variables a, b, c, d, and e
print(a)            #prints the value of a (1)
print(b)            #prints the value of b (2)
print(c)            #prints the value of c (3)
print(d)            #prints the value of d (4)
print(e)            #prints the value of e (5)  

#tuple count
print(tup_1.count(3))  #counts the number of occurrences of the element 3 in tup_1 and prints the result (1)
print(tup_1.count(6))  #counts the number of occurrences of the element 6 in tup_1 and prints the result (0)

#tuple index
print(tup_1.index(3))  #finds the index of the first occurrence of the element 3 in tup_1 and prints it (2)
print(tup_1.index(6))  #tries to find the index of the element 6 in tup_1, but since it is not present, it raises a ValueError

#tuple immutability
try:
    tup_1[0] = 10  #attempts to change the first element of tup_1 to 10, but since tuples are immutable, it raises a TypeError
except TypeError as e:
    print(e)  #prints the error message indicating that tuples do not support item assignment

# tuple concatenation with different types
tup_8 = tup_1 + (11, 12)  #concatenates tup_1 with another tuple containing 11 and 12, and assigns it to tup_8
print(tup_8)  #prints the concatenated tuple (1, 2, 3, 4, 5, 11, 12)

# tuple repetition with different types
tup_9 = tup_1 * 3  #repeats tup_1 three times and assigns it to tup_9
print(tup_9)  #prints the repeated tuple (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# tuple slicing with negative indices
tup_10 = tup_1[-4:-1]  #slices tup_1 from index -4 to index -2 (since -1 is exclusive) and assigns it to tup_10
print(tup_10)  #prints the sliced tuple (2, 3, 4)

# tuple slicing with out of range indices
tup_11 = tup_1[0:10]  #slices tup_1 from index 0 to index 9 (10 is exclusive) and assigns it to tup_11
print(tup_11)  #prints the sliced tuple (1, 2, 3, 4, 5) since the end index is out of range, it stops at the last element of the tuple

# tuple unpacking with different number of variables
try:
    a, b, c = tup_1  #attempts to unpack the elements of tup_1 into three variables a, b, and c, but since there are more than three elements in the tuple, it raises a ValueError
except ValueError as e:
    print(e)  #prints the error message indicating that the number of variables does not match the number of elements in the tuple

# tuple unpacking with nested tuples
tup_12 = (1, 2, (3, 4), 5)  #creates a tuple that contains another tuple (3, 4) as one of its elements
a, b, (c, d), e = tup_12  #unpacks the elements of tup_12 into variables a, b, c, d, and e, where c and d are unpacked from the nested tuple (3, 4)
print(a)  #prints the value of a (1)

# prints the value of b (2)
print(b)
print(c)  #prints the value of c (3)
print(d)  #prints the value of d (4)
print(e)  #prints the value of e (5)

# tuple concatenation with different types
tup_13 = tup_1 + (11, 12) + ('a', 'b')  #concatenates tup_1 with another tuple containing 11 and 12, and then concatenates it with another tuple containing 'a' and 'b', and assigns it to tup_13
print(tup_13)  #prints the concatenated tuple (1, 2, 3, 4, 5, 11, 12, 'a', 'b')

#   tuple repetition with different types
tup_14 = tup_1 * 2 + ('a', 'b') * 2  #repeats tup_1 twice and concatenates it with another tuple containing 'a' and 'b' repeated twice, and assigns it to tup_14
print(tup_14)  #prints the repeated and concatenated tuple (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 'a', 'b', 'a', 'b')

#   tuple slicing with step and negative indices
tup_15 = tup_1[-1:0:-2]  #slices tup_1 from index -1 to index 1 (since 0 is exclusive) with a step of -2, meaning it takes every second element in reverse order, and assigns it to tup_15
print(tup_15)  #prints the sliced tuple (5, 3)

# tuple slicing with out of range indices and step
tup_16 = tup_1[0:10:2]  #slices tup_1 from index 0 to index 9 (10 is exclusive) with a step of 2, meaning it takes every second element, and assigns it to tup_16
print(tup_16)  #prints the sliced tuple (1, 3, 5) since the end index is out of range, it stops at the last element of the tuple

# tuple unpacking with different number of variables and nested tuples
try:
    a, b, c, d = tup_12  #attempts to unpack the elements of tup_12 into four variables a, b, c, and d, but since there are only three elements in the tuple (the nested tuple is considered as one element), it raises a ValueError
except ValueError as e:
    print(e)  #prints the error message indicating that the number of variables does not match the number of elements in the tuple

