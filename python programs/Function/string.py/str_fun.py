str_1="i am learning python"
str_2="python is a programming language"

#concatination
str_3=str_1+" "+str_2   #concatenates str_1 and str_2 with a space in between
print(str_3)            #prints the concatenated string

#repetition
str_4=str_1*2           #repeats str_1 twice and assigns it to str_4
print(str_4)            #prints the repeated string

#slicing
str_5=str_1[2:8]         #slices str_1 from index 2 to index 7 (8 is exclusive) and assigns it to str_5
print(str_5)             #prints the sliced string
str_6=str_1[2:]          #slices str_1 from index 2 to the end of the string and assigns it to str_6
print(str_6)             #prints the sliced string

#length
print(len(str_1))        #prints the length of str_1
print(len(str_2))        #prints the length of str_2

#membership
print("python" in str_1)    #checks if the substring "python" is present in str_1 and prints the result (True or False)
print("python" in str_2)    #checks if the substring "python" is present in str_2 and prints the result (True or False)

#string methods
print(str_1.upper())   #converts to uppercase
print(str_2.lower())  #converts to lowercase
print(str_1.split())  #splits the string into a list of words

#string formatting
name="Alice"
age=30
print("My name is {} and I am {} years old.".format(name, age))  #formats the string using the format method
print(f"My name is {name} and I am {age} years old.")            #formats the string using f-strings (available in Python 3.6 and later)

#string concatenation using join
words=["Hello", "world", "from", "Python"]
sentence=" ".join(words)                                          #joins the list of words into a single string with spaces in between
print(sentence)                                                   #prints the joined string

#string slicing with step
str_7=str_1[::2]                   #slices str_1 with a step of 2, meaning it takes every second character
print(str_7)                       #prints the sliced string with step 

#string reverse
str_8=str_1[::-1]                  #slices str_1 with a step of -1, which reverses the string
print(str_8)                       #prints the reversed string

#string find
index=str_1.find("python")          #finds the index of the first occurrence of "python" in str_1
print(index)                        #prints the index of the substring "python" in str_1 (returns -1 if not found)
index=str_2.find("python")          #finds the index of the first occurrence of "python" in str_2
print(index)                        #prints the index of the substring "python" in str_2 (returns -1 if not found)

#string replace
str_9=str_1.replace("python", "Java")   #replaces the substring "python" with "Java" in str_1 and assigns it to str_9
print(str_9)                            #prints the modified string with "python" replaced by "Java in str_1
str_10=str_2.replace("python", "Java")  #replaces the substring "python" with "Java" in str_2 and assigns it to str_10
print(str_10)                           #prints the modified string with "python" replaced by "Java

#string strip
str_11="   Hello, World!   "              #a string with leading and trailing whitespace assigned to str_11 
print(str_11.strip())                     #removes leading and trailing whitespace from str_11 and prints the result 

#string startswith and endswith
print(str_1.startswith("i am"))           #checks if str_1 starts with the substring "i am" and prints the result (True or False)
print(str_1.endswith("python"))          #checks if str_1 ends with the substring "python" and prints the result (True or False)

#string count
count=str_1.count("python")          #counts the number of occurrences of the substring "python" in str_1 and assigns it to count
print(count)                         #prints the count of occurrences of "python" in str_1 
count=str_2.count("python")          #counts the number of occurrences of the substring "python" in str_2 and assigns it to count
print(count)                         #prints the count of occurrences of "python" in str_2 

#string isalpha, isdigit, isspace
print(str_1.isalpha())               #checks if all characters in str_1 are alphabet
print(str_1.isdigit())               #checks if all characters in str_1 are digits
print(str_1.isspace())               #checks if all characters in str_1 are whitespace

#string formatting with alignment
print("{:<20}".format("Left aligned"))   #left-aligns the string within a
print("{:>20}".format("Right aligned"))  #right-aligns the string within a
print("{:^20}".format("Center aligned")) #center-aligns the string within a

#string formatting with padding
print("{:*>20}".format("Padded"))         #pads the string with '*' on
print("{:0>20}".format("Padded"))         #pads the string with '0' on the left
print("{:0<20}".format("Padded"))         #pads the string with '0' on the right

#string formatting with precision
pi=3.141592653589793
print("Pi to 2 decimal places: {:.2f}".format(pi))  #formats pi to 2 decimal places using the format method
print(f"Pi to 2 decimal places: {pi:.2f}")          #formats pi to 2 decimal places using f-strings

#string formatting with thousands separator
number=1234567890
print("Number with thousands separator: {:,}".format(number))  #formats the number with a thousands separator using the format method
print(f"Number with thousands separator: {number:,}")          #formats the number with a thousands separator using f-strings

#string formatting with percentage
percentage=0.12345
print("Percentage: {:.2%}".format(percentage))  #formats the percentage to 2 decimal places and adds a '%' sign using the format method
print(f"Percentage: {percentage:.2%}")          #formats the percentage to 2 decimal places and adds a '%' sign using f-strings

#string formatting with scientific notation
number=1234567890
print("Number in scientific notation: {:.2e}".format(number))  #formats the number in scientific notation with 2 decimal places using the format method
print(f"Number in scientific notation: {number:.2e}")          #formats the number in scientific notation with 2 decimal places using f-strings

#string formatting with hexadecimal, octal, and binary
number=255
print("Number in hexadecimal: {:x}".format(number))  #formats the number in hexadecimal using the format method
print(f"Number in hexadecimal: {number:x}")          #formats the number in hexadecimal using f-strings
print("Number in octal: {:o}".format(number))       #formats the number in octal using the format method
print(f"Number in octal: {number:o}")             #formats the number in octal using f-strings
print("Number in binary: {:b}".format(number))      #formats the number in binary using the format method
print(f"Number in binary: {number:b}")            #formats the number in binary using f-strings

#string formatting with custom format specifier
number=123.456
print("Custom format: {:*>10.2f}".format(number))  #formats the number with a custom format specifier using the format method
print(f"Custom format: {number:*>10.2f}")          #formats the number with a custom format specifier using f-strings

#string formatting with dictionary
data={"name": "Alice", "age": 30}
print("My name is {name} and I am {age} years old.".format(**data))  #formats the string using a dictionary with the format method
print(f"My name is {data['name']} and I am {data['age']} years old.")  #formats the string using a dictionary with f-strings

#string formatting with list
data=["Alice", 30]
print("My name is {} and I am {} years old.".format(*data))  #formats the string using a list with the format method
print(f"My name is {data[0]} and I am {data[1]} years old.")  #formats the string using a list with f-strings

#string formatting with tuple
data=("Alice", 30)
print("My name is {} and I am {} years old.".format(*data))  #formats the string using a tuple with the format method
print(f"My name is {data[0]} and I am {data[1]} years old.")  #formats the string using a tuple with f-strings

#string formatting with set
data={"Alice", 30}
print("My name is {} and I am {} years old.".format(*data))  #formats the string using a set with the format method (note: sets are unordered, so the output may vary)
print(f"My name is {data.pop()} and I am {data.pop()} years old.")  #formats the string using a set with f-strings (note: sets are unordered, so the output may vary)

#string formatting with custom class
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
person=Person("Alice", 30)
print("My name is {} and I am {} years old.".format(person.name, person.age))  #formats the string using a custom class with the format method
print(f"My name is {person.name} and I am {person.age} years old.")  #formats the string using a custom class with f-strings

#string formatting with nested fields
data={"person": {"name": "Alice", "age": 30}}
print("My name is {person[name]} and I am {person[age]} years old.".format(**data))  #formats the string using nested fields in a dictionary with the format method
print(f"My name is {data['person']['name']} and I am {data['person']['age']} years old.")  #formats the string using nested fields in a dictionary with f-strings

#string formatting with nested fields and custom format specifier
data={"person": {"name": "Alice", "age": 30}}
print("My name is {person[name]:<10} and I am {person[age]:>5} years old.".format(**data))  #formats the string using nested fields in a dictionary with a custom format specifier using the format method
print(f"My name is {data['person']['name']:<10} and I am {data['person']['age']:>5} years old.")  #formats the string using nested fields in a dictionary with a custom format specifier using f-strings

#string formatting with nested fields and custom format specifier and precision
data={"person": {"name": "Alice", "age": 30.12345}}
print("My name is {person[name]:<10} and I am {person[age]:>10.2f} years old.".format(**data))  #formats the string using nested fields in a dictionary with a custom format specifier and precision using the format method
print(f"My name is {data['person']['name']:<10} and I am {data['person']['age']:>10.2f} years old.")  #formats the string using nested fields in a dictionary with a custom format specifier and precision using f-strings

#string formatting with nested fields and custom format specifier and precision and thousands separator
data={"person": {"name": "Alice", "age": 12345.6789}}
print("My name is {person[name]:<10} and I am {person[age]:>20,.2f} years old.".format(**data))  #formats the string using nested fields in a dictionary with a custom format specifier, precision, and thousands separator using the format method
print(f"My name is {data['person']['name']:<10} and I am {data['person']['age']:>20,.2f} years old.")  #formats the string using nested fields in a dictionary with a custom format specifier, precision, and thousands separator using f-strings

#string formatting with nested fields and custom format specifier and precision and thousands separator and percentage
data={"person": {"name": "Alice", "age": 0.12345}}
print("My name is {person[name]:<10} and I am {person[age]:>20,.2%} years old.".format(**data))  #formats the string using nested fields in a dictionary with a custom format specifier, precision, thousands separator, and percentage using the format method
print(f"My name is {data['person']['name']:<10} and I am {data['person']['age']:>20,.2%} years old.")  #formats the string using nested fields in a dictionary with a custom format specifier, precision, thousands separator, and percentage using f-strings

#string formatting with nested fields and custom format specifier and precision and thousands separator and percentage and scientific notation
# Note: This example may not make much sense in a real-world scenario, but it demonstrates the use of multiple format specifiers together.
data={"person": {"name": "Alice", "age": 0.12345}}
print("My name is {person[name]:<10} and I am {person[age]:>20,.2e} years old.".format(**data))  #formats the string using nested fields in a dictionary with a custom format specifier, precision, thousands separator, percentage, and scientific notation using the format method
print(f"My name is {data['person']['name']:<10} and I am {data['person']['age']:>20,.2e} years old.")  #formats the string using nested fields in a dictionary with a custom format specifier, precision, thousands separator, percentage, and scientific notation using f-strings

#string formatting with nested fields and custom format specifier and precision and thousands separator and percentage and scientific notation and hexadecimal
# Note: This example may not make much sense in a real-world scenario, but it demonstrates the use of multiple format specifiers together.
data={"person": {"name": "Alice", "age": 255}}
print("My name is {person[name]:<10} and I am {person[age]:>20,.2x} years old.".format(**data))  #formats the string using nested fields in a dictionary with a custom format specifier, precision, thousands separator, percentage, scientific notation, and hexadecimal using the format method
print(f"My name is {data['person']['name']:<10} and I am {data['person']['age']:>20,.2x} years old.")  #formats the string using nested fields in a dictionary with a custom format specifier, precision, thousands separator, percentage, scientific notation, and hexadecimal using f-strings

#string formatting with nested fields and custom format specifier and precision and thousands separator and percentage and scientific notation and hexadecimal and octal
# Note: This example may not make much sense in a real-world scenario, but it demonstrates
#the use of multiple format specifiers together.
data={"person": {"name": "Alice", "age": 255}}
print("My name is {person[name]:<10} and I am {person[age]:>20,.2o} years old.".format(**data))  #formats the string using nested fields in a dictionary with a custom format specifier, precision, thousands separator, percentage, scientific notation, hexadecimal, and octal using the format method
print(f"My name is {data['person']['name']:<10} and I am {data['person']['age']:>20,.2o} years old.")  #formats the string using nested fields in a dictionary with a custom format specifier, precision, thousands separator, percentage, scientific notation, hexadecimal, and octal using f-strings







    