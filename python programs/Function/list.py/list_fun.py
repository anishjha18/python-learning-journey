# append
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
# a.append(6)    # it will add 6 at the end of list a
# b.append(7)    # it will add 7 at the end of list b
# print(a)       # it will print the list a after appending
# print(b)       # it will print the list b after appending

# # len
# print(len(a))  # it will return the length of list a
# print(len(b))  # it will return the length of list b

# # extend
# a.extend(b)    # it will add all elements of list b to the end of list a
# print(a)       # it will print the list a after extending
# print(b)       # it will print the list b after extending

# # insert
# a.insert(2, 10)  # it will insert 10 at index 2
# b.insert(3, 15)  # it will insert 15 at index 3
# print(a)         # it will print the list a after insertion
# print(b)         # it will print the list b after insertion

# # delete
# print(a)   # it will print the list a before deletion
# del a[2]   # it will delete the element at index 2
# print(a)   # it will print the list a after deletion
# print(b)   # it will print the list b before deletion
# del b[3]   # it will delete the element at index 3
# print(b)   # it will print the list b after deletion

# # remove
# print(a)      # it will print the list a before removing
# a.remove(3)   # it will remove the first occurrence of 3 from list a
# print(a)      # it will print the list a after removing
# print(b)      # it will print the list b before removing
# b.remove(6)   # it will remove the first occurrence of 6 from list b
# print(b)      # it will print the list b after removing

# pop
# print(a)      # it will print the list a before popping
# c=a.pop(1)       # it will remove and return the last element of list a
# print(a)      # it will print the list a after popping
# print(b)      # it will print the list b before popping
# b.pop()       # it will remove and return the last element of list b
# print(b)      # it will print the list b after popping
# print(c)

# # clear
# a.clear()    # it will remove all elements from list a
# print(a)      # it will print the list a after clearing
# print(len(a))  # it will return the length of list a after clearing
# b.clear()    # it will remove all elements from list b
# print(b)      # it will print the list b after clearing
# print(len(b))  # it will return the length of list b after clearing

# # index
# a = [1, 2, 3, 4, 5, 10]
# b = [5, 6, 7, 8, 9, 15]
# print(a.index(4))  # it will return the index of first occurrence of 4
# print(b.index(7))  # it will return the index of first occurrence of 7
# print(a.index(10))  # it will return the index of first occurrence of 10
# print(b.index(15))  # it will return the index of first occurrence of 15

# # count
# print(a.count(2))  # it will return the count of occurrences of 2 in list a
# print(b.count(6))  # it will return the count of occurrences of 6 in list b
# print(a.count(5))  # it will return the count of occurrences of 5 in list a
# print(b.count(9))  # it will return the count of occurrences of 9 in list b

# # sort
# a.sort()    # it will sort the list a in ascending order
# print(a)    # it will print the sorted list a
# b.sort()    # it will sort the list b in ascending order
# print(b)    # it will print the sorted list b
# a.sort(reverse=True)  # it will sort the list a in descending order
# print(a)    # it will print the sorted list a in descending order
# b.sort(reverse=True)  # it will sort the list b in descending order
# print(b)    # it will print the sorted list b in descending order

# # reverse
# a.reverse()   # it will reverse the list a
# print(a)      # it will print the reversed list a
# b.reverse()   # it will reverse the list b
# print(b)      # it will print the reversed list b

# # copy
# c = a.copy()  # it will create a copy of list a and assign it to c
# d = b.copy()  # it will create a copy of list b and assign it to d
# print(c)      # it will print the copied list c
# print(d)      # it will print the copied list d

# # del
# del c[0]      # it will delete the element at index 0 from list c
# print(c)      # it will print the list c after deletion
# del d[1]      # it will delete the element at index 1 from list d
# print(d)      # it will print the list d after deletion

# # sorted
# e = sorted(a)  # it will return a new sorted list from the elements of a
# print(e)        # it will print the sorted list e
# f = sorted(b)  # it will return a new sorted list from the elements of b
# print(f)        # it will print the sorted list f
# # it will return a new sorted list from a in descending order
# e_desc = sorted(a, reverse=True)
# print(e_desc)   # it will print the sorted list e in descending order
# # it will return a new sorted list from b in descending order
# f_desc = sorted(b, reverse=True)
# print(f_desc)   # it will print the sorted list f in descending order

# # list()
# g = list((10, 20, 30, 40))   # it will create a list from the given tuple
# print(g)                     # it will print the list g
# h = list('a', 'b', 'c', 'd') # it will create a list from the given set
# print(h)                     # it will print the list h
# i = list('hello', 'world')   # it will create a list from the given set
# print(i)                     # it will print the list i
# j = list('python')           # it will create a list from the given string
# print(j)                     # it will print the list j
# k = list('function')         # it will create a list from the given string
# print(k)                     # it will print the list k

# # membership test
# print(10 in g)       # it will return True if 10 is in list g else False
# print('a' in h)      # it will return True if 'a' is in
# print('hello' in i)  # it will return True if 'hello' is in list i else False
# print('py' in j)     # it will return True if 'py' is in
# print('fun' in k)    # it will return True if 'fun' is in list k else False
# print(50 in g)       # it will return True if 50 is in list g else False
# print('z' in h)      # it will return True if 'z' is in list h else False
# print('hi' in i)     # it will return True if 'hi' is in list i else False
# print('java' in j)   # it will return True if 'java' is in list j else False
# print('code' in k)   # it will return True if 'code' is in list k else False
# print(20 not in g)   # it will return True if 20 is not in list g else False
# print('b' not in h)  # it will return True if 'b' is not in list h else False


# #max
# print(max(a))  # it will return the maximum element from list a
# print(max(b))  # it will return the maximum element from list b

# #min
# print(min(a))  # it will return the minimum element from list a
# print(min(b))  # it will return the minimum element from list b

# #sum
# print(sum(a))  # it will return the sum of all elements in list a
# print(sum(b))  # it will return the sum of all elements in list b

# #average
# print(sum(a)/len(a))  # it will return the average of elements in list a
# print(sum(b)/len(b))  # it will return the average of elements in list b

# #filter
# even_a = list(filter(lambda x: x % 2 == 0, a))
# print(even_a)  # it will print the list of even numbers from list a
# even_b = list(filter(lambda x: x % 2 == 0, b))
# print(even_b)  # it will print the list of even numbers from list b
# odd_a = list(filter(lambda x: x % 2 != 0, a))
# print(odd_a)   # it will print the list of odd numbers from list a
# odd_b = list(filter(lambda x: x % 2 != 0, b))
# print(odd_b)   # it will print the list of odd numbers from list b

# #map
# squared_a = list(map(lambda x: x**2, a))
# print(squared_a)  # it will print the list of squares of elements in list a
# squared_b = list(map(lambda x: x**2, b))
# print(squared_b)  # it will print the list of squares of elements in list b
# cubed_a = list(map(lambda x: x**3, a))
# print(cubed_a)    # it will print the list of cubes of elements in list a
# cubed_b = list(map(lambda x: x**3, b))
# print(cubed_b)    # it will print the list of cubes of elements in list b

# #reduce
# from functools import reduce               # it will import reduce function from functools module
# product_a = reduce(lambda x, y: x * y, a)  # it will return the product of all elements in list a
# print(product_a)                           # it will print the product of elements in list a
# product_b = reduce(lambda x, y: x * y, b)  # it will return the product of all elements in list b
# print(product_b)                           # it will print the product of elements in list b

# #enumerate
# for index, value in enumerate(a):             # it will iterate through list a with index and value
#     print(f"Index: {index}, Value: {value}")  # it will print index and value of each element in list a
# for index, value in enumerate(b):
#     print(f"Index: {index}, Value: {value}")  # it will print index and value of each element in list b

# #zip
# zipped = list(zip(a, b)) # it will zip the two lists a and b into a list of tuples
# print(zipped)  # it will print the zipped list of tuples from lists a and b

# #unzip
# unzipped_a, unzipped_b = zip(*zipped) # it will unzip the zipped list into two separate lists
# print(list(unzipped_a))  # it will print the unzipped list a
# print(list(unzipped_b))  # it will print the unzipped list b

# #list comprehension
# squared_comp_a = [x**2 for x in a] # it will create a list of squares of elements in list a using list comprehension
# print(squared_comp_a)  # it will print the list of squares of elements in list a using list comprehension
# squared_comp_b = [x**2 for x in b]
# print(squared_comp_b)  # it will print the list of squares of elements in list b using list comprehension
# cubed_comp_a = [x**3 for x in a]
# print(cubed_comp_a)    # it will print the list of cubes of elements in list a using list comprehension
# cubed_comp_b = [x**3 for x in b]
# print(cubed_comp_b)    # it will print the list of cubes of elements in list b using list comprehension

# #nested list comprehension
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = [num for row in matrix for num in row]
# print(flattened)  # it will print the flattened list from the nested list (matrix)

# #list slicing
# print(a[1:4])  # it will print the sublist of a from index 1 to 3
# print(b[2:5])  # it will print the sublist of b from index 2 to 4
# print(a[:3])   # it will print the first three elements of list a
# print(b[:4])   # it will print the first four elements of list b
# print(a[2:])   # it will print the elements of list a from index 2 to end
# print(b[3:])   # it will print the elements of list b from index 3 to end
# print(a[-3:])  # it will print the last three elements of list a
# print(b[-2:])  # it will print the last two elements of list b
# print(a[:-2])  # it will print all elements of list a except the last two
# print(b[:-3])  # it will print all elements of list b except the last three

# #list multiplication
# multiplied_a = a * 3
# print(multiplied_a)  # it will print the list a repeated 3 times
# multiplied_b = b * 2
# print(multiplied_b)  # it will print the list b repeated 2 times

# #list addition
# added_lists = a + b
# print(added_lists)  # it will print the concatenated list of a and b

# #list subtraction
# subtracted_a = [item for item in a if item not in b]
# print(subtracted_a)  # it will print the list of elements in a not in b
# subtracted_b = [item for item in b if item not in a]
# print(subtracted_b)  # it will print the list of elements in b not in a

# #list multiplication with condition
# conditional_multiplied_a = [x * 2 for x in a if x % 2 == 0]
# print(conditional_multiplied_a)  # it will print the list of even elements in a multiplied by 2
# conditional_multiplied_b = [x * 3 for x in b if x % 2 != 0]
# print(conditional_multiplied_b)  # it will print the list of odd elements in b multiplied by 3

# #list addition with condition
# conditional_added_lists = [x + y for x, y in zip(a, b) if x % 2 == 0 and y % 2 == 0]
# print(conditional_added_lists)  # it will print the list of sums of even elements from a and b
