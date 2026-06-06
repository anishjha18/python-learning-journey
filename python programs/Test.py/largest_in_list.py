# n=int(input("Enter the size of the list :"))
# a = []
# for i in range (n) :
#     m = int(input("Enter the number : "))
#     a.append(m)
# print("Your entered list is : ",a)
# l = a[0]
# for i in range(n) :
#     if a[i] > l :
#         l = a[i]
# print(l," is the largest number in the list")

# ***********************************************

# n=int(input("Enter the size of the list : "))
# a = []
# for i in range(n) :
#     m = int(input("Enter the number : "))
#     a.append(m)
# print("Your entered list is : ",a)
# a.sort(reverse = True)
# l = a[0]
# for i in range(n) :
#     if a[i] < l:
#         l = a[i]
#         break
# print(l," is the second largest number in the list")

# ***********************************************


# # Read size and list
# n = int(input("Enter the size of the list: "))
# a = []
# for i in range(n):
#     m = int(input("Enter the number: "))
#     a.append(m)

# print("Your entered list is:", a)

# # Remove duplicates and sort in descending order
# unique = []
# for x in a:
#     if x not in unique:
#         unique.append(x)
# unique.sort(reverse=True)

# # Decide if there is a second largest
# if len(unique) < 2:
#     print("There is no second largest number.")
# else:
#     print(unique[1], "is the second largest number in the list.")
