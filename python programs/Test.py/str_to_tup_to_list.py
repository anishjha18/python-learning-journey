# String to tuple to list conversion
values =input("Enter comma-separated values:\n ")
tup=tuple(values.split(","))
lst=list(tup)
print("Tuple:", tup)
print("List:", lst)
